import pandas as pd

def load_annotation(annotation_file: str) -> pd.DataFrame:
    """
    Загружает данные из файла аннотации в DataFrame

    :param annotation_file: путь к файлу аннотации
    
    """
    return pd.read_csv(annotation_file, names=["absolute_path", "relative_path"], header=0)