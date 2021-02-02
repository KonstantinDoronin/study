#функция поиска минимального элемента в последовательности значений
def min(*a):
    m = a[0]
    for i in a:
        if m > i:
            m = i
    return m
print(min(5,2,3,4))