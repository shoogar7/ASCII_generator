from PIL import Image, ImageOps

def load_image():
    # loading file_name of image from predefined variable, could later add console or UI
    file_name = "image.jpg"
    # file_name = str(input("Provide name of the image file: "))

    # create Image object with Pillow
    with Image.open(file_name) as image:
            
        # loading output size of image from predefined variable, could later add console or UI
        ascii_width = 50
        # we assume the image is vertical and calculate height (can add automatic detection later)
        ascii_height = ascii_width * 2

        # resizing the image
        image = image.resize((ascii_width, ascii_height))

        # testing another options for resizing the image
        # image = ImageOps.fit(image, (ascii_width, ascii_height))

        # to make it easier to translate into ASCII, we convert the image to black-white
        image = image.convert("L")

        # testing how the image looks for now
        # image.show()

def main():
    load_image()

if __name__ == "__main__":
    main()