import cv2

def read_image(image_path):
    """
    Чтение изображения.

    :param image_path: Path to hte image
    
    """
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image dont found: {image_path}")
    return image

def image_size(image):
    """
    Вывод размера изображения.
    
    """
    print(f"Size pic: {image.shape[1]}x{image.shape[0]} px")
