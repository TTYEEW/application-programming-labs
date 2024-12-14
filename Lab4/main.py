from parser import parse
from data_frame import (load_annotation, 
                        add_rows_for_image,
                        filter_images,
                        plot_area_histogram,
                        sort_by_area)

## Add files via upload ###
def main() -> None:
    try:
        arg = parse()
        df = load_annotation(arg.annotation_file)
        add_rows_for_image(df)
        df = filter_images(df, arg.max_height, arg.max_width)
        df =sort_by_area(df)
        print(df)
        plot_area_histogram(df)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()