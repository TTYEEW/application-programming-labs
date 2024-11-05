import argparse
import re
from collections import Counter

##
def parse() -> str:
    """
    Парсинг аргументов командной строки
    :return: путь к файлу

    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str, help='data.txt')
    return parser.parse_args().file_path

def file_read(path_to_file: str) -> str:
    """
    Прочесть файл и вернуть его содержимое
    :param path-to_file: путь к файлу с анкетами
    :return: содержимое файла(текст)

    """
    try:
        with open(path_to_file, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File {path_to_file} not found.")
    except Exception as e:
        raise Exception(f"Error reading file {e}")

def find_phone_pattern(data: str) -> tuple[str, int]:
    """
    Найти наиболее часто встречающийся код оператора и вернуть его и количество раз, которое он встречается
    :param data: текст из файла с анкетами
    :return: наиболее часто встречающийся код оператора 

    """
    phone_pattern = re.findall(r'\b\d{3}\b', data)
    number_of_codes = Counter(phone_pattern)
    if number_of_codes :
        return number_of_codes.most_common(1)
    else: None

def main() -> None:
    try:
        data = file_read(parse())
        common_code = find_phone_pattern(data)
        if common_code:
            print(f"The most common code: {common_code[0][0]} is encountered {common_code[0][1]} times")
        else:
            print("Phone numbers not found")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()