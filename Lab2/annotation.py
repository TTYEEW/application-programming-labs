import csv
import os

def create_annatation_file(directory: str, annotation_file: str):
    with open(annotation_file, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Absolute Path', 'Relative Path'])
        for root, _, images in os.walk(directory):
            for image in images:
                if image.lower().endswith(('.png', '.jpg', '.jpeg')):
                    absolute_path = os.path.join(root, image)
                    relative_path = os.path.relpath(absolute_path, directory)
                    writer.writerow([absolute_path, relative_path])
