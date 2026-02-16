from PIL import Image, ImageOps

def load_image():
    # loading file_name of image from predefined variable, could later add console or UI
    file_name = "image.jpg"
    # file_name = str(input("Provide name of the image file: "))

    # create Image object with Pillow
    with Image.open(file_name) as image:
            
        # loading output size of image from predefined variable, could later add console or UI
        ascii_width = 100
        # we assume the image is vertical and calculate height (can add automatic detection later)
        ascii_height = ascii_width * 2

        # resizing the image
        image = ImageOps.fit(image,(ascii_width, ascii_height))

        # testing another options for resizing the image
        # image = ImageOps.fit(image, (ascii_width, ascii_height))

        # to make it easier to translate into ASCII, we convert the image to black-white
        image = image.convert("L")

        # testing how the image looks for now
        # image.show()

        # data = list(image.getdata())

        data = image.get_flattened_data()
        # print(len(data))

        # print(data[:100])
        
        # # @ % = + * -   
        # 0-36 #
        # 37-72 @
        # 73-109 %
        # 110-145 =
        # 146-182 +
        # 183-218 *
        # 219-255 -

        # print(data)

        with open("ascii.txt", "w") as file:
            line = ""
            content = ""
            for i, pixel in enumerate(data):
                if (pixel>=0 and pixel<=36):
                    line+="#"
                elif (pixel>=37 and pixel<=72):
                    line+="@"
                elif (pixel>=73 and pixel<=109):
                   line+="%"
                elif (pixel>=110 and pixel<=145):
                    line+="="
                elif (pixel>=146 and pixel<=182):
                    line+="+"
                elif (pixel>=183 and pixel<=218):
                    line+="*"
                elif (pixel>=219 and pixel<=255):
                    line+="-"
                # print(i)
                if i%ascii_width == 0:
                    line+="\n"
                    content+=line
                    # clearing the line holder to not save the history of making the art ;=;
                    line = ""
                    # print(line)
            file.write(content)

def main():
    load_image()

if __name__ == "__main__":
    main()