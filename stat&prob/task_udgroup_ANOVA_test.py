import pandas as pd
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import *
from matplotlib import pyplot as plt
from matplotlib import rc
import numpy as np
from sklearn.cluster import KMeans
# Загрузим данные из xls документа
# При необходимости надо изменить название файла и листа, на котором находятся данные
# Проще всего файл положить в папку, где находиться и сам скрипт. В это случае укажите только название
# sheet_name - название листа, с котрого надо загрузить данные
data = pd.read_excel(r'C:\Users\kv.doronin\Desktop\DataScience — копия\UDG\test\UDG_0907.xlsx')
# команда data.head() выводит первые пять строчек загруженных в переменную дата данных
print(data.tail())
print(data.corr())
# посомтрим основные статистические параметры данных
print(data.describe())