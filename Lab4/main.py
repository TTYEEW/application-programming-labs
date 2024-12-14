from parser import parse
from data_frame import (load_annotation, 
                        add_rows_for_image,
                        filter_images,
                        plot_area_histogram,
                        sort_by_area,
                        decsriber)

## Add files via upload ###
def main() -> None:
    try:
        arg = parse()
        df = load_annotation(arg.annotation_file)
        print(f"Add path to image\n {df}")
        add_rows_for_image(df)
        print(f"Add rows for image\n{df}")
        dfg = filter_images(df, arg.max_height, arg.max_width)
        print(f"Fultered images\n {dfg}")
        df = sort_by_area(df)
        print(f"Sorted images\n {df}")
        
        plot_area_histogram(df)
        
        decsriber(df)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()