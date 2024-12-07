import cv2
import matplotlib.pyplot as plt
import os
from numpy import ndarray

import matplotlib
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

def plot_histogram(image: ndarray, file_name: str) -> None:
    """
    Build and save an image histogram

    :param image: arr image
    :param file_name: name of the histogram
    
    """
    plt.figure(figsize=(12, 6))
    
    for i, color in enumerate(('b', 'g', 'r')):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color, label=f"{color.upper()} channel")
    
    plt.title("Image Histogram")
    plt.xlabel("Pixels range")
    plt.ylabel("Pixels count")
    plt.legend(loc="upper left")

    plt.savefig(file_name)
    print(f"Histogram save in: {os.path.abspath(file_name)}")
    plt.close()


def resize_image(image: ndarray, width: int, height: int) -> ndarray:
    """
    Change size image(overlay_img)
    
    """
    return cv2.resize(image, (width, height))

def mixing_images(input_image: ndarray, overlay_image: ndarray, transparency: float) -> ndarray:
    """
    Overlay two images with a specified transparency
    
    """
    transparency = max(0, min(1, transparency))
    return cv2.addWeighted(input_image, 1 - transparency, overlay_image, transparency, 0)

def compare_images(image1: ndarray, image2: ndarray, file_name: str) -> None:
    """
    Compare images


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
    print(f"Compare images: {os.path.abspath(file_name)}")
    plt.close()


def save_image(image: ndarray, output_path: str) -> None:
    """
    Save image
    
    :param image: arr image
    :param output_path: path to save
    """
    if output_path and not os.path.exists(output_path):
        os.makedirs(output_path)

    output_path = os.path.join(output_path, "result.png")
    cv2.imwrite(output_path, image)
    print(f"Result in: {os.path.abspath(output_path)}")