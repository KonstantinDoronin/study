import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.tree import export_graphviz
plt.style.use('ggplot')
data = pd.read_excel(r'C:\Users\kv.doronin\Desktop\GP_watcom_test.xlsx', na_values='?')#подгружаем данные в данных содержатся пустые ячейки
categorical_columns = [c for c in data.columns if data[c].dtype.name == 'object']
numerical_columns = [c for c in data.columns if data[c].dtype.name != 'object']
print(categorical_columns)
print(numerical_columns)
writer = pd.ExcelWriter(r'C:\Users\kv.doronin\Desktop\num_corr.xlsx', engine='xlsxwriter')#записываем статистику по категорийным данным на отдельный лист
mydata = data.corr()#сохраняем данные по корреляциям в файл
mydata.to_excel(writer,'corr')
writer.save()
data_describe = data.describe(include=[object])
binary_columns = [c for c in categorical_columns if data_describe[c]['unique'] == 2]#!!!!рахбиваем категорийные столбцы на бинарные и множественно-категорийные
nonbinary_columns = [c for c in categorical_columns if data_describe[c]['unique'] > 2]
print(binary_columns, nonbinary_columns)
data_nonbinary = pd.get_dummies(data[nonbinary_columns])
print(data_nonbinary.columns)
data_numerical = data[numerical_columns]
data_numerical = (data_numerical - data_numerical.mean()) / data_numerical.std()
print(data_numerical.describe())
data = pd.concat((data_numerical, data[binary_columns], data_nonbinary), axis=1)
data = pd.DataFrame(data, dtype=float)
print(data.shape)
print(data.columns)
writer = pd.ExcelWriter(r'C:\Users\kv.doronin\Desktop\error.xlsx', engine='xlsxwriter')#записываем статистику по категорийным данным на отдельный лист
mydata = data#сохраняем данные по корреляциям в файл
mydata.to_excel(writer,'error')
writer.save()
X = data.drop(('x39_E'), axis=1)  # Выбрасываем столбец 'class'.
y = data['x39_E'].round().astype((int)) #переводим float в  int . иначе ошибка при обучении
print(y.head())
writer = pd.ExcelWriter(r'C:\Users\kv.doronin\Desktop\error.xlsx', engine='xlsxwriter')#записываем статистику по категорийным данным на отдельный лист
mydata = y#сохраняем данные по корреляциям в файл
mydata.to_excel(writer,'error')
writer.save()
feature_names = X.columns
print(feature_names)
print(X.shape)
print(y.shape)
N, d = X.shape
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 11)
N_train, _ = X_train.shape
N_test,  _ = X_test.shape
print(N_train, N_test)
rf = ensemble.RandomForestClassifier(n_estimators=100, random_state=11)
rf.fit(X_train, y_train)
err_train = np.mean(y_train != rf.predict(X_train))
err_test = np.mean(y_test != rf.predict(X_test))
print(err_train, err_test)
importances = rf.feature_importances_
indices = np.argsort(importances)[::-1]
print("Feature importances:")
for f, idx in enumerate(indices):
    print("{:2d}. feature '{:5s}' ({:.4f})".format(f + 1, feature_names[idx], importances[idx]))
d_first = 20
plt.figure(figsize=(8, 8))
plt.title("Feature importances_Раз в месяц")
plt.bar(range(d_first), importances[indices[:d_first]], align='center')
plt.xticks(range(d_first), np.array(feature_names)[indices[:d_first]], rotation=90)
plt.xlim([-1, d_first])
plt.show()
estimator_limited = rf.estimators_[5]
print(estimator_limited)
