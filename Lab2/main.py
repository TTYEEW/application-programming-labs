from annotation import create_annatation_file
from imgdownload import download_image
from iterator import ClassIterator
from parser import parse

def main() -> None:
    try:
        arg = parse()
        download_image(arg.directory, arg.key, arg.value)
        create_annatation_file(arg.directory, arg.annotation_file)
        for img in ClassIterator(arg.annotation_file):
            print(img)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()