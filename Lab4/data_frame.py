import cv2
import pandas as pd

def load_annotation(annotation_file: str) -> pd.DataFrame:
    """
    Загружает данные из файла аннотации в DataFrame

    :param annotation_file: путь к файлу аннотации
    
    """
    return pd.read_csv(annotation_file, names=["absolute_path", "relative_path"], header=0)

def add_rows_for_image(df: pd.DataFrame) -> None:
    """
    Добавляет столбцы высоты, ширины, глубины и площади изображений
    
    """
    heights, widths, depths, areas = [], [], [], []
    for _, row in df.iterrows():
        image = cv2.imread(row["absolute_path"])
        if image is not None:
            h, w, d = image.shape
            heights.append(h)
            widths.append(w)
            depths.append(d)
            areas.append(h * w)
        else:
            raise FileNotFoundError(f"image {row["absolute_path"]} not found")

    df["height"] = heights
    df["width"] = widths
    df["depth"] = depths
    df["area"] = areas