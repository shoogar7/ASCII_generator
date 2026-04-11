from PIL import Image
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pyperclip
import click

def copy_art_to_clipboard(art):
    try:
        pyperclip.copy(art)
        print("Art succesfully copied to the clipboard!")
    except:
        print("ERROR: An error occured!")

def generate_art(data, ascii_width):
    prepared_art = "" # placeholder
    with open("ascii.txt", "w") as file:
            content = "" # placeholder 

            ascii_palette = ('.', ',', '-', '~', '+', '=', 'x', '9', 'X', '%', '$', '@', '#')
            ascii_count = len(ascii_palette)
            MAX_LIGHT_VAL = 256
            
            # calculate ascii index for every pixel
            for light_val in data:
                content += ascii_palette[(light_val * ascii_count) // MAX_LIGHT_VAL]

            # slice the data into rows and store 
            for i in range(0, len(data), ascii_width):
                 prepared_art += content[i:i+ascii_width] + "\n"
            file.write(prepared_art)
            return prepared_art

def pick_size(image, size): # image obj; size in string from (small, medium, big)
    ascii_width = image.width
    ascii_height = image.height
    proportions = 1
    
    # assign adequate size
    if size == "s":
        shorter_edge = 100
    if size == "m":
        shorter_edge = 150
    if size == "b":
        shorter_edge = 200
    
    # calculate art size
    if ascii_width < ascii_height: # vertical
        ascii_width = shorter_edge
        proportions += ascii_width / ascii_height
        ascii_height = ascii_width * proportions
    elif ascii_height < ascii_width: # horizontal
        ascii_height = shorter_edge
        proportions += ascii_height / ascii_width
        ascii_width = ascii_height * proportions
    else: # square
        return shorter_edge, int(shorter_edge * 0.5) # ascii are a lot higher than wider
            
    return int(ascii_width), int(ascii_height * 0.5) # has to be int, float could cause crashes

def get_image():
    tk.Tk().withdraw()
    try:
        return askopenfilename(title="Select an image to generate art from.")
    except:
        print("ERROR: Wrong file type!")
        return 0

def load_image(file, size):
    try:
        with Image.open(file) as image: # create Image object with Pillow     
            ascii_width, ascii_height = pick_size(image, size) 
            # print(f"width:{ascii_width} height:{ascii_height}")

            image = image.resize((ascii_width, ascii_height))
            # image.show()

            image = image.convert("L") # convert to black and white for easier ASCII translation
            data = image.get_flattened_data()
                    
            return generate_art(data, ascii_width) # take the preprocessed data and turn it into art
    except:
        print("ERROR: File has to be an image!")

def inner_machinations(file, copy):
    if not file:
        file = click.prompt("Specify a file path. (Can leave empty for a file picker pop-up.)\n", default='')
        if not file:
            file = get_image()
        
    size = click.prompt("Specify size of the art. Default is 'm' - 150.\n", default="m")
    art = load_image(file, size)   
    
    if copy:
        copy_art_to_clipboard(art)

    click.echo(art)
        
    return art, file

@click.command()
@click.option('--copy', is_flag=True, help='Copy art to your Clipboard.') 
def art_cli(copy):
    file = None
    click.echo('''\nSimple ASCII art generator.\nThe art is automatically saved to "ascii.txt".
          If you don't provide path to image, a dialog window will pop up. 
          You can choose size from:
          "s" - small, 
          "m" - medium, 
          "b" - big \nType '--copy' to copy to clipboard or "--help" for more.\n''')
    
    while True:
        art, file = inner_machinations(file, copy)
        
        response = click.prompt('''What would you like to do? \nExit [x] \nCopy [c] \nChange size [s] \nCreate another art [Enter]\n''', default='')
        if response == '':
            file = None
            continue
        if response == 'c':
            file = None
            copy_art_to_clipboard(art)
            break
        if 'c' in response:
            copy_art_to_clipboard(art)
        if 'x' in response:
            break
        if 's' in response:
            continue
        else:
            break

if __name__ == "__main__":
    art_cli()