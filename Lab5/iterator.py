import csv
import os

class ClassIterator:
    """
    Итератор для перебора изображений в файле аннотации.

    """
    def __init__(self, annotation_file: str):
        self.images = []
        self.index = 0
        if not os.path.exists(annotation_file):
            raise FileNotFoundError("Файл аннотации не найден.")
        with open(annotation_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for line in reader:
                abs_path = line[0]
                self.images.append(abs_path)

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.index < len(self.images):
            image_path = self.images[self.index]
            self.index += 1
            return image_path
        raise StopIteration
