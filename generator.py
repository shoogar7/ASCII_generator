from PIL import Image
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pyperclip

def generate_art(data, ascii_width):
    prepared_art = "" # placeholder
    with open("ascii.txt", "w") as file:
            content = "" # placeholder 

            ascii_palette = (".", "'", "-", "+", "*", "=", "x", "X", "%", "#")
            ascii_count = len(ascii_palette)
            MAX_LIGHT_VAL = 256
            
            # calculate ascii index for every pixel
            for light_val in data:
                content += ascii_palette[(light_val * ascii_count) // MAX_LIGHT_VAL]

            # slice the data into rows and store 
            for i in range(0, len(data), ascii_width):
                 prepared_art += content[i:i+ascii_width] + "\n"
            file.write(prepared_art)
    copy_art_to_clipboard(prepared_art)

def pick_size(image, size): # image obj; size in string from (small, medium, big)
    ascii_width = image.width
    ascii_height = image.height
    proportions = 1
    
    # SIZE = {"S": 100, "M": 150, "B": 200}
    # assign adequate size
    if size == "small":
        shorter_edge = 100
    if size == "medium":
        shorter_edge = 150
    if size == "big":
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
            
    # print(f"width:{ascii_width} height:{ascii_height} proportions:{proportions}")
    return int(ascii_width), int(ascii_height * 0.5) # has to be int, float could cause crashes

def load_image():
    tk.Tk().withdraw()
    try:
        file_name = askopenfilename(title="Select an image to generate art from.")
    except:
        print("ERROR: Wrong file!")
        return 0
    
    try:
        with Image.open(file_name) as image: # create Image object with Pillow     
            ascii_width, ascii_height = pick_size(image, "big") 
            # print(f"width:{ascii_width} height:{ascii_height}")

            image = image.resize((ascii_width, ascii_height))
            # image.show()

            image = image.convert("L") # convert to black and white for easier ASCII translation
            data = image.get_flattened_data()
                    
            generate_art(data, ascii_width) # take the preprocessed data and turn it into art
    except:
        print("ERROR: File has to be an image!")

def copy_art_to_clipboard(art):
    try:
        pyperclip.copy(art)
        print("Art succesfully copied to the clipboard!")
    except:
        print("ERROR: An error occured!")

def main():
    load_image()

if __name__ == "__main__":
    main()