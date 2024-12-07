from parser import parse
from image_utility import (
    read_image, image_size
)

def main():
    args = parse()
    image = read_image(args.input)
    image_size(image)


if __name__ == "__main__":
    main()