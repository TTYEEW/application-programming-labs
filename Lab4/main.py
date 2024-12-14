from parser import parse
from data_frame import (load_annotation)

##Add files via upload
def main() -> None:
    try:
        arg = parse()
        df = load_annotation(arg.annotation_file)
        print(df)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()