import pandas as pd


def convert_to_csv(path_txt: str, path_csv_out: str):
    dataframe = pd.read_csv(path_txt)
    dataframe.to_csv(path_csv_out)
