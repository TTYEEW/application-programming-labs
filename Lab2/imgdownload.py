import os
from icrawler.builtin import GoogleImageCrawler

def download_image(directory: str, key: str, val: int) -> None:
    if not os.path.exists(directory):
        os.makedirs(directory)
    google_crawler = GoogleImageCrawler(storage={'root_dir': directory, "backend": "FileSystem"})
    google_crawler.crawl(keyword=key, max_num=val)