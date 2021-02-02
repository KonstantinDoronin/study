import pandas as pd
import numpy as np
data = pd.read_excel(r'C:\Users\kv.doronin\Desktop\test_2.xlsx', na_values='?')#подгружаем данные в данных содержатся пустые ячейки
print(data.head())
df = data.loc[data.index.repeat(data.times)]
print(df.head())
writer = pd.ExcelWriter(r'C:\Users\kv.doronin\Desktop\test_output_2.xlsx')
df.to_excel(writer, sheet_name = 'test')
writer.save()