from parser import parse
from image_utility import (
    read_image, image_size, plot_histogram, resize_image,
    blend_images, compare_images, save_image
)

def main():
    args = parse()

    image = read_image(args.input)
    image_size(image)
    plot_histogram(image, "histogram_of_input")

    overlay_image = read_image(args.overlay)
    image_size(overlay_image)
    plot_histogram(overlay_image, "histogram_of_over")

    overlay_resized = resize_image(overlay_image, image.shape[1], image.shape[0])

    blended_image = blend_images(image, overlay_resized, args.transparency)

    compare_images(image, blended_image, "compare.png")

    save_image(blended_image, args.output)

if __name__ == "__main__":
    main()