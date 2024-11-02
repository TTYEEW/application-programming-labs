import argparse
from imgdownload import download_image

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('key', type = str, help = "Keyword for photo search")
    parser.add_argument('-dir', '--directory', type = str, help = "The path to the directory")
    parser.add_argument('-val', '--value', type = int, help = "Number of images to download")
    arg = parser.parse_args()
    download_image(arg.directory, arg.key, arg.value)

if __name__ == "__main__":
    main()