#функция, выполняющая 3 условия в зависимости от переменноя x
def equal(x):#sozdaem funkciu s odnoq ishodnoy peremennoy na vhode
    sum = 0.0#sozdaem localnui peremennuk
    if x <= -2:# cicle na 3 uslovia
        sum = 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        sum = -x / 2
    elif x > 2:
        sum = (x - 2) ** 2 + 1
    return sum#chto na vyhode
print(equal(10.5))