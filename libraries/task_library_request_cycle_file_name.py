import requests #импортируем библиотеку запросов к сайтам requests
with open('/Users/user/Desktop/dataset_3378_3.txt') as inf:#отркывам файл построчно
    for line in inf:
        line = line.strip()#построчное открытие файла
print(line)
temp = line[::-1]#создаем строку line наоборот для обрезки последнего адреса
basa = ''
asap = ''
check = '123'#вводим любые значения для первого условия в цикле
d = ''
while check[0] != '"':#цикл на проверку последнего символа в строке line адреса сайта
    r = requests.get(line)#запрашиваем файл по адресу в строке line
    print(r.text)
    basa = temp[temp.find('/'):]#поиск первого значения(с обратной стророны)
    asap = basa[::-1]
    print(asap)
    line = asap + r.text#добавляем последнее значение из нового файла в строку line
    d = line
    check = d[::-1]#обратная строка line - для проверки на значение первого элемента
    print(check[0])
    print(check)
    print(line)


