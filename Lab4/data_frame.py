import cv2
import matplotlib.pyplot as plt
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

    :param df: Данные из файла аннотации
    
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

def filter_images(df: pd.DataFrame, max_height: int, max_width: int) -> pd.DataFrame:
    """
    Фильтрует DataFrame по заданным размерам изображений

    :param df: данные из аннотации уже с height, width, depth, area
    :param max_height: максимальная высота
    :param max_width: максимальная высота

    """
    return df[(df["height"] <= max_height) & (df["width"] <= max_width)]

def sort_by_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Сортирует DataFrame по площади изображений (от min к max)

    :param df: Данные
    
    """
    return df.sort_values(by="area")

def plot_area_histogram(df: pd.DataFrame) -> None:
    """
    Строит гистограмму распределения площадей изображений
    
    """
    plt.hist(df["area"].dropna(), bins=20, edgecolor="black", color="skyblue")
    plt.title("Распределение площадей изображений")
    plt.xlabel("Площадь (пиксели)")
    plt.ylabel("Частота")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

def decsriber(df: pd.DataFrame):

    print(f"Add describer\n{df[["height","width","depth"]].describe()}")
