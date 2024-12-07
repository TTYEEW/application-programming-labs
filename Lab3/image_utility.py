import cv2
import matplotlib
import matplotlib.pyplot as plt
import os

from numpy import ndarray


matplotlib.use('Agg')

def read_image(image_path: str) -> ndarray:
    """
    Read image

    :param image_path: Path to hte image
    
    """
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Image dont found: {image_path}")
    return image

def image_size(image: ndarray) -> None:
    """
    Output size image

    :param image: arr image
    
    """
    print(f"Size pic: {image.shape[1]}x{image.shape[0]} px")

def plot_histogram(image: ndarray) -> dict:
    """
    Build histogram

    :param image: arr image
    :param file_name: name of the histogram
    
    """
    histograms = {}
    for i, color in enumerate(('blue', 'green', 'red')):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        histograms[color] = hist
    return histograms


def save_histogram(histograms: dict, file_name: str) -> None:
    """
    Build figure of histogram

    :param histograms: histograms for BLUE GREEN RED
    :param file_name: name of the histogram
    """

    fig, ax = plt.subplots(figsize=(12, 6))
    for color, hist in histograms.items():
        ax.plot(hist, color=color, label=f"{color.upper()} channel")
    
    ax.set_title("Image Histogram")
    ax.set_xlabel("Pixels range")
    ax.set_ylabel("Pixels count")
    ax.legend(loc="upper left")
    
    fig.savefig(file_name)
    plt.close(fig)


def resize_image(image: ndarray, width: int, height: int) -> ndarray:
    """
    Change size image(overlay_img)

    :param width: width
    :param height: height
    
    """
    return cv2.resize(image, (width, height))

def mixing_images(input_image: ndarray, overlay_image: ndarray, transparency: float) -> ndarray:
    """
    Overlay two images with a specified transparency

    :param input_image: original image
    :param overlay_image: image which mixed with original
    :param transparency: transparency of overlay image (0-1)
    
    """
    transparency = max(0, min(1, transparency))
    return cv2.addWeighted(input_image, 1 - transparency, overlay_image, transparency, 0)

def compare_images(image1: ndarray, image2: ndarray, file_name: str) -> None:
    """
    Compare images

    :param image1: input_image
    :param image2: mixed_image
    :param file_name: name to save the file

    """
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
    plt.title("Input_image")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
    plt.title("Overlay_image")
    plt.axis('off')

    plt.savefig(file_name)
    plt.close()


def save_image(image: ndarray, output_path: str) -> None:
    """
    Save image
    
    :param image: arr image
    :param output_path: path to save

    """
    path_exist = os.path.exists(os.path.split(output_path)[0])
    path_not_empty = os.path.split(output_path)[0]

    if path_not_empty and not path_exist:
        os.makedirs(os.path.split(output_path)[0])
    
    cv2.imwrite(output_path, image)