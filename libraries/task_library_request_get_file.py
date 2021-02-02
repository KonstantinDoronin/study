import requests #импортируем библиотеку запросов к сайтам
with open('/Users/user/Desktop/dataset_3378_2.txt', 'r') as inf:#открываем файл с сылкой
    for line in inf:#построчно считываем файл с сылкой построчно
        line = line.strip()#построчное считывание файла
        print(line)
r = requests.get(line)#запрашиваем информацию по ссылке line
cnd = 0
for i in r.text:#подсчитываем количество символов '\n' в тексте файла
    if i == '\n':#счетчик символов '\n' в тексте файла
        cnd += 1
print(cnd)#