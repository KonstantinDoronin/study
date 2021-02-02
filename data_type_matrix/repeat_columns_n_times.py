import pandas as pd
import numpy as np
data = pd.read_excel(r'C:\Users\kv.doronin\Desktop\test.xlsx', na_values='?')#подгружаем данные в данных содержатся пустые ячейки
print(data.head())
df = pd.DataFrame(pd.np.tile(data, (208, 1)))#повторяем столбец заданное количество раз и записываем его в тот же столбец
print(df)
writer = pd.ExcelWriter(r'C:\Users\kv.doronin\Desktop\test_output.xlsx')
df.to_excel(writer, sheet_name = 'test')
writer.save()