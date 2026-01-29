def load_image():
    # loading file_name of image from predefined variable, could later add console or UI
    file_name = "image.jpg"
    # file_name = str(input("Provide name of the image file: "))

    # checking file_name extention, could later check from a list or add a variable
    if file_name[-1:-5:-1] != "gnp." and file_name[-1:-5:-1] != "gpj.":
        print("Wrong file format")
    else:
        print(f"Generating ASCII from {file_name}")

def main():
    load_image()

if __name__ == "__main__":
    main()