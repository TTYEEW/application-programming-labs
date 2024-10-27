import argparse
import re
from collections import Counter

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str, help='data.txt')
    return parser.parse_args().file_path

def file_read(path_to_file):
    try:
        with open(path_to_file, 'r', encoding='utf-8') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File {path_to_file} not found.")
    except Exception as e:
        raise Exception(f"Error reading file {e}")

def main():
    data = file_read(parse())
    phone_pattern = re.findall(r'\b\d{3}\b', data)
    number_of_codes = Counter(phone_pattern)
    common_code = number_of_codes.most_common(1)

    if common_code:
        print(f"The most common code: {common_code[0][0]} is encountered {common_code[0][1]} times")
    else:
        print("Phone numbers not found")

if __name__ == "__main__":
    main()