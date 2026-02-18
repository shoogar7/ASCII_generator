from PIL import Image, ImageOps

# data - from which generate the art
# width - to be sure when the line ends
def generate_art(data, ascii_width):
    with open("ascii.txt", "w") as file:
            content = "" # placeholder 

            ASCII_chars = ("#", "@", "%", "=", "+", "*", "-")
            ASCII_count = len(ASCII_chars)
            MAX_LIGHT_VAL = 256
            
            # calculate ascii index for every pixel
            for light_val in data:
                content += ASCII_chars[(light_val * ASCII_count) // MAX_LIGHT_VAL]

            final_content = "" # storing data before saving to file

            # slice the data into rows and store 
            for i in range(0, len(data), ascii_width):
                 final_content += content[i:i+ascii_width] + "\n"
                
            # # saving the art to designated file
            file.write(final_content)

def load_image():
    # loading file_name of image from predefined variable, could later add console or UI
    file_name = "image.jpg"
    # file_name = str(input("Provide name of the image file: "))

    # create Image object with Pillow
    with Image.open(file_name) as image:
            
        # loading output size of image from predefined variable, could later add console or UI
        ascii_width = 150
        # we assume the image is vertical and calculate height (can add automatic detection later)
        # parsing to int because float crashes
        ascii_height = (int)(ascii_width * 1.05)

        # resizing the image
        image = image.resize((ascii_width, ascii_height))

        # testing another options for resizing the image
        # image = ImageOps.fit(image, (ascii_width, ascii_height))

        # to make it easier to translate into ASCII, we convert the image to black-white
        image = image.convert("L")

        # testing how the image looks for now
        # image.show()

        data = image.get_flattened_data()
        # print(len(data))
        
        # take the preprocessed data and turn it into art
        generate_art(data, ascii_width)

def main():
    load_image()

if __name__ == "__main__":
    main()