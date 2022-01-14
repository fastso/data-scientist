import pandas as pd

xls_data = pd.ExcelFile('test.xls')

print(xls_data.sheet_names)

df1 = xls_data.parse(0)

print(df1.head())

df2 = xls_data.parse('Sheet2')

print(df2.head())

# 1行目スキップ、カラム名のリネーム
df1 = xls_data.parse(0, skiprows=[0], names=['Index','Value01', 'Value02'])
print(df1.head())

# 1列目指定、1行目スキップ、カラム名のリネーム
df2 = xls_data.parse('Sheet2', usecols=[0], skiprows=[0], names=['インデックス'])
print(df2.head())

