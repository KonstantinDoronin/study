#функция, которая просто несколько раз вызывает себя (рекурсивная)

def f(n): #zadaem imya i argumenty funkcii
    return n * 10 + 5 #chto vozvrachaem(cnto delaet funkciya)
print(f(f(f(10)))) #output
