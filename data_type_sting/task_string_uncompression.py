#задача: сделать расшифровку из файла (а3 = ааа)
#
#
with open('/Users/user/Desktop/dataset_3363_2.txt', 'r') as inf: #открываем файл для чтения исходных данных
    for line in inf:
        a = line.strip()
c = '1,2,3,4,5,6,7,8,9,0'# делаем список с цифрами (для сравнения переменных из исходных данных)
bukva = ''
temp = 0
cnt = 0
schet = 0
file = ''
for j in range(0, len(a)):# так как работать будем по индексам
    if j + 1 < len(a): # условие,  для всех кроме последнего значения списка(так как иначе будет переполнение)
        if a[j] not in c: # условие- проверка на букву, если буква - то следующий аргумент
            bukva = a[j]
            cnt = 0    #обязательно обнуляем сумматор
            continue
        elif a[j] in c: #проверка - значение есть в списке цифр
            if a[j + 1] not in c and a[j - 1] not in c:#если рядом только буквы
                cnt = a[j]
            elif a[j + 1] in c and a[j - 1] not in c:#если справа цифра - то завершаем проверку - следующий
                continue
            elif a[j + 1] not in c and a[j - 1] in c: #если справа буква -то считаем цифры слева
                cnt = a[j - 1] + a[j]
    schet = int(cnt) * bukva #умножаем сумматор на букву и записываем в список
    file += schet
    if j + 1 == len(a): #для последнего элемента возможно несколько вариантов (0 или 00 цифра)
        if a[j - 1] not in c: #  для цифры
            schet = int(a[j]) * bukva
            file += schet
        elif a[j - 1] in c: # для числа (00)
            schet = int(a[j - 1] + a[j]) * bukva
            file += schet
print(file)
out = open('/Users/user/Desktop/text.txt', 'w')  #записываем последовательность в файлик
out.write(file)