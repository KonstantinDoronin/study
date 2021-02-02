import pandas as pd
import pandas_profiling
data = pd.read_excel(r'C:\Users\kv.doronin\Desktop\GP_podarki_2019.xlsx', na_values='?')
print(data.head())
df = data
df["Возраст"].fillna(df["Возраст"].mean(), inplace=True)#заполняем средним по столбцу возраст
df.fillna(0, inplace=True)#заполняем 0 вместо Nan
print(df)
writer = pd.ExcelWriter(r'C:\Users\kv.doronin\Desktop\error.xlsx', engine='xlsxwriter')#записываем статистику по категорийным данным на отдельный лист
mydata = df
mydata.to_excel(writer,'data')
writer.save()
profile = pandas_profiling.ProfileReport(data)
profile.to_file(r"C:\Users\kv.doronin\Desktop\report.html")