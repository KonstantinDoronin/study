#ввод чисел до тех пора, пока их сумма не станет равной нулю.
#после этого, возведение числа в квадрат

a = int(input()) #int value input
s = a #nachalnoe prisvoeynie peremennoy
deg = 0 #vvod peremennoy
while s != 0: #cikl poka s != 0
    deg += a ** 2 #vozvedenie v kvadrat - do proverki uslovya
    if s != 0: #proverka uslovia s!= 0
        a = int(input()) #vvod sleduuchey variable a
        s += a #dobavleniye var a v s
deg += a ** 2 #vozvedeniy poslednego znachenia a v kvadrat
print(deg) #vyvod