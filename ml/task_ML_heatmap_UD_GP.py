import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
data = pd.read_excel(r'C:\Users\kv.doronin\Desktop\Посещаемость_ГП_Python\082018\test.xlsx', na_values='?')#подгружаем данные в данных содержатся пустые ячейки
ax = plt.axes()
sns.heatmap(data.corr(), annot=True)
ax.set_title('bill_0')
plt.show()