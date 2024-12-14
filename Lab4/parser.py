import argparse

def parse() -> argparse.Namespace:
    """
    Парсинг аргументов командной строки

    :return arg: Возвращение аргументов командной строки

    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', '--annotation_file', type = str, help = "Path to annotation")
    parser.add_argument('-max_width', type = int, help = "Max_width")
    parser.add_argument('-max_height', type = int, help = "Max_height")
    arg = parser.parse_args()
    return arg