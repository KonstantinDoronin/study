import pandas as pd
import numpy as np
df = pd.read_excel(r'C:\Users\kv.doronin\Desktop\Акция ТЦ _ГоркиПарк_ - Розыгрыш автомобиля_122019_магазины_2.xlsx', na_values='?', sheet_name='data_1')#подгружаем данные в данных содержатся пустые ячейки
print(df.head())
df['Какие магазины вы обычно посещаете в ТЦ "ГоркиПарк"?'] = df['Какие магазины вы обычно посещаете в ТЦ "ГоркиПарк"?'].map(lambda x: ', '.join(sorted(x.split(', '))))
print(df.head())
writer = pd.ExcelWriter(r'C:\Users\kv.doronin\Desktop\test_output_3.xlsx')#запишем в Excel
df.to_excel(writer, sheet_name = 'test')
writer.save()