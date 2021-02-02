#opredelenie schasliviy ili net bylet ((6-ty znachniy)
a = int(input())
a1, a2, a3, a4, a5, a6 = int(a % 10), int(a % 100), int(a % 1000), int(a % 10000), int(a % 100000), int(a % 1000000)
#vydeleniy kagdoy cifry
if a1 + (a2 - a1) / 10 + (a3 - a2) / 100 == (a4 - a3) / 1000 + (a5 - a4) / 10000 + (a6 - a5) / 100000:
    print('Счастливый') #kogda summa pervih 3 ravna summe poslednyh 3
else:
    print('Обычный')#vse ostalniy sluchayi
