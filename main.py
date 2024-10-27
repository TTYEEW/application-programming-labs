import argparse

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

if __name__ == "__main__":
    main()