import csv
import os

def create_annatation_file(directory: str, annotation_file: str) -> None:
    """
    Функция для создания аннотации

    :param directory: Папка с изображениями
    :param annotation_file: Путь для создания аннотации

    """
    with open(annotation_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Absolute Path', 'Relative Path'])
        for root, _, images in os.walk(directory):
            for image in images:
                if image.lower().endswith(('.png', '.jpg', '.jpeg')):
                    absolute_path = os.path.abspath(os.path.join(root, image))
                    relative_path = os.path.join(root, image)
                    writer.writerow([absolute_path, relative_path])