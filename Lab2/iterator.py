import csv

class ClassIterator:
    """
    Итератор для перебора изображений в заданной директории.

    """
    def __init__(self, annotation_file: str):
        """
        Перебирает пути к изображениям из файла аннотаций
        :param annotation_file: путь к файлу с аннотациями

        """
        self.images = []
        self.index = 0
        with open(annotation_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for line in reader:
                abs_path = line[1]
                self.images.append(abs_path)

    def __iter__(self) -> 'ClassIterator':
        return self
    
    def __next__(self) -> str:
        """
        Возвращает следующий уникальный путь к файлу изображения.

        :return image_path: Путь к следующему файлу изображения.

        """
        if self.index < len(self.images):
            image_path = self.images[self.index]
            self.index += 1
            return image_path

        raise StopIteration
