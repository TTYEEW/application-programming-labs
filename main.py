import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str, help='data.txt')
    return parser.parse_args().file_path

def file_read(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as file:
        data = file.read()
    return data

def main():
    data = file_read(parse())

if __name__ == "__main__":
    main()