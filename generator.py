from PIL import Image

def generate_art(data, ascii_width):
    with open("ascii.txt", "w") as file:
            content = "" # placeholder 

            ascii_chars = (".", "'", "-", "+", "*", "=", "x", "X", "%", "#")
            ascii_count = len(ascii_chars)
            MAX_LIGHT_VAL = 256
            
            # calculate ascii index for every pixel
            for light_val in data:
                content += ascii_chars[(light_val * ascii_count) // MAX_LIGHT_VAL]

            final_content = "" # placeholder

            # slice the data into rows and store 
            for i in range(0, len(data), ascii_width):
                 final_content += content[i:i+ascii_width] + "\n"
                
            file.write(final_content)

def pick_size(image, size): # image obj; size in string from (small, medium, big)
        
    ascii_width = image.width
    ascii_height = image.height
    proportions = 1
    
    # SIZE = {"S": 100, "M": 150, "B": 200}
    if size == "small":
        shorter_edge = 100
    if size == "medium":
        shorter_edge = 150
    if size == "big":
        shorter_edge = 200
    
    if ascii_width < ascii_height:
        ascii_width = shorter_edge
        proportions += ascii_width / ascii_height
        ascii_height = int(ascii_width * proportions)
    elif ascii_height < ascii_width:
        ascii_height = shorter_edge
        proportions += ascii_height / ascii_width
        ascii_width = int(ascii_height * proportions)
    else:
        return shorter_edge, int(shorter_edge * 0.5) # ascii are a lot higher than wider
            
    print(f"width:{ascii_width} height:{ascii_height} proportions:{proportions}")
    return ascii_width, int(ascii_height * 0.5) 

def load_image(file): # file - from which make art; 
    file_name = file  
    
    with Image.open(file_name) as image: # create Image object with Pillow     
        
        ascii_width, ascii_height = pick_size(image, "big") 
        print(f"width:{ascii_width} height:{ascii_height}")

        image = image.resize((ascii_width, ascii_height))
        # image.show()

        image = image.convert("L") # convert to black and white for easier ASCII translation

        data = image.get_flattened_data()
                
        generate_art(data, ascii_width) # take the preprocessed data and turn it into art

def main():
    load_image("image3.png")

if __name__ == "__main__":
    main()