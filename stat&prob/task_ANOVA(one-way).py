import pandas as pd  # импортируем панду для работы с данными
import researchpy as rp  # импортируем для статистики
import scipy.stats as stats  # импортируем для проведения ANOVA
from statsmodels.formula.api import ols  # ANOVA с более расширенными данными

df = pd.read_csv(r'C:\Users\kv.doronin\Desktop\DataScience — копия\data\genetherapy.csv')
print(df.head())# читаем файл, при необходимости удаляем лишние столбцы через drop
print(rp.summary_cont(df['expr'].groupby(df['Therapy'])))  # получаем общую статистику
print(
    stats.f_oneway(df['expr'][df['Therapy'] == 'A'], df['expr'][df['Therapy'] == 'B'], df['expr'][df['Therapy'] == 'C'],
                   df['expr'][df['Therapy'] == 'D']))
# на выходе получаем F-value значение теста и Pvalue из F-распределения (Фишера) - если меньше 0,05 - то отвергаем H0)
# число элементов в выборке по виду терапии (столбец Therapy)
# среднее значение экспрессии гена (столбец expr)
# стандартное отклонение (столбец expr)
# стандартная ошибка (столбец expr)
#
#
results = ols('expr ~ C(Therapy)', data=df).fit()
print(results.summary())
# описание результатов: группы различные (p-ratio = 0,00015 )
# а именно различия между группами А и С и А и D (А и B - похожи - p = 0,598)
