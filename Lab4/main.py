from parser import parse
from data_frame import (load_annotation, 
                        add_rows_for_image)

##Add files via upload
def main() -> None:
    try:
        arg = parse()
        df = load_annotation(arg.annotation_file)
        add_rows_for_image(df)
        print(df)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()