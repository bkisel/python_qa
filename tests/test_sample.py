import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.validators import load_csv, load_excel, check_column_exist
# read csv file
# def test_id_column_exists():
#     df = load_csv('data/db.csv')
#     assert check_column_exist(df, 'id')
#     assert check_column_exist(df, 'name')
#     assert check_column_exist(df, 'age')

# def test_open_file():
#     df = load_csv('data/db.csv')
#     print('\n', df)

# read excel file
# def test_read_excel():
#     df = load_excel('data/test.xlsx', sheet='Аркуш2')
#     print('\n', df)

# join two data frames
# import pandas as pd

# df1 = pd.DataFrame({
#     'id': [1, 2],
#     'name': ['Anna', 'Bob']
# })

# df2 = pd.DataFrame({
#     'id': [1, 2],
#     'age': [28, 32]
# })

# # Джойн по колонці 'id'
# merged_df = pd.merge(df1, df2, on='id', how='inner')
# print(merged_df)

## як розпарсити вкладені json'и
import json
from jsonpath_ng import parse

with open('data/data.json', 'r') as f:
    data = json.load(f)

json_expr = parse('user.address.city')
matches = json_expr.find(data)
print(matches[0].value)

