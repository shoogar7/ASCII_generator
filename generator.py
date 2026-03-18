from PIL import Image

def generate_art(data, ascii_width):
    with open("ascii.txt", "w") as file:
            content = "" # placeholder 

            ascii_chars = ("#", "@", "%", "=", "+", "*", "-")
            ascii_count = len(ascii_chars)
            MAX_LIGHT_VAL = 256
            
            # calculate ascii index for every pixel
            for light_val in data:
                content += ascii_chars[(light_val * ascii_count) // MAX_LIGHT_VAL]

            final_content = "" # storing data before saving to file

            # slice the data into rows and store 
            for i in range(0, len(data), ascii_width):
                 final_content += content[i:i+ascii_width] + "\n"
                
            file.write(final_content) # saving the art to designated file

def load_image():
    file_name = "image.png" # example  
    
    with Image.open(file_name) as image: # create Image object with Pillow      
        ascii_width = 150 # example  
        
        # temporarily we assume the image is vertical and calculate height
        ascii_height = (int)(ascii_width * 1.05) # have to parse to int; float causes crashing

        image = image.resize((ascii_width, ascii_height))
        image = image.convert("L") # convert to black and white for easier ASCII translation

        data = image.get_flattened_data()
                
        generate_art(data, ascii_width) # take the preprocessed data and turn it into art

def main():
    load_image()

if __name__ == "__main__":
    main()