from image_utility import (
    read_image, image_size, plot_histogram, resize_image,
    mixing_images, compare_images, save_image, save_histogram
)
from parser import parse

##
def main():
    try:
        args = parse()

        image = read_image(args.input)
        image_size(image)
        dict1 = plot_histogram(image)
        save_histogram(dict1, "input_histogam.png")

        overlay_image = read_image(args.overlay)
        image_size(overlay_image)
        dict2 = plot_histogram(overlay_image)
        save_histogram(dict2,"overlay_histogram.png")

        overlay_resized = resize_image(overlay_image, image.shape[1], image.shape[0])

        blended_image = mixing_images(image, overlay_resized, args.transparency)

        compare_images(image, blended_image, "compare.png")

        save_image(blended_image, args.output)
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()