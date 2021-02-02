#функция, которая убирает все нечетные значения , а четные - преобразует (делит на 2)
def modify_list(l):#sozdaem funkciuy
    b = [int(x) for x in l if int(x) % 2]#soadaem spisok iz vseh nechetniy znacheniy spiska l
    for i in b:#cycle na udaleniye nechetnih znacheniy iz l (l - b)
        if i in l:
            l.remove(i)
    for i in range(len(l)):#cycle na deleniye vseh znacheniy cycla l na 2 - delaem cherez index
        l[i] = int(l[i] / 2)
l = [0, -1, -3, 12, 12, 18, 19, 21, 20] #ishodniy spisok
modify_list(l)
print(l)