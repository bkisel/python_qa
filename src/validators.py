import pandas as pd

def load_csv(path):
    return  pd.read_csv(path)

def load_excel(path, sheet):
    return pd.read_excel(path, sheet_name=sheet)

def check_column_exist(df, column_name):
    return column_name in df.columns