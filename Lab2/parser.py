import argparse

def parse() -> tuple[str, str, int, str]:
    """
    Парсинг аргументов командной строки

    """
    parser = argparse.ArgumentParser()
    parser.add_argument('key', type = str, help = "Keyword for photo search")
    parser.add_argument('-dir', '--directory', type = str, help = "The path to the directory")
    parser.add_argument('-val', '--value', type = int, help = "Number of images to download")
    parser.add_argument('-file', '--annotation_file', type = str, help = "Path to annotation")
    arg = parser.parse_args()
    return arg