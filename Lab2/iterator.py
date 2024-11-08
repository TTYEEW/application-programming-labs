
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
            next(file)
            for line in file:
                parts = line.strip().split(',')
                abs_path = parts[1]
                self.images.append(abs_path)
        #Отладка
        print(f"Найдено {len(self.images)} изображений")

    def __iter__(self) -> 'ClassIterator':
        return self
    
    def __next__(self) -> str:
        """
        Возвращает следующий уникальный путь к файлу изображения.

        :return str: Путь к следующему файлу изображения.

        """
        while self.index < len(self.images):
            image_path = self.images[self.index]
            self.index += 1
            return image_path

        raise StopIteration
