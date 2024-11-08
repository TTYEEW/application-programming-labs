import os
from icrawler.builtin import GoogleImageCrawler

def download_image(directory: str, key: str, val: int) -> None:
    """
    Функция для скачивания заданных изображений

    :param directory: Путь для сохранения изображений
    :param key: Ключ для поиска изображений
    :param val: Кол-во изображений 

    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    google_crawler = GoogleImageCrawler(storage={'root_dir': directory, "backend": "FileSystem"})
    google_crawler.crawl(keyword=key, max_num=val)