#построение матрицы размерностью n в виде змейки стремящейся к центру

n = int(input())
a = [[0] * n for i in range(n)] #sozdaem nulevuym matricu
k = n // 2 #opredelyaem kolivhestvo krugov
temp = 1
nach = 0
konch = n
for i in range(k):#bolshoy cycle po kolichestvu kvadratov
    for di in range(nach + i, n - i):#cycle verhnih strok
        for dj in range(nach + i, n - i):
            while a[di][dj] == 0:
                a[di][dj] += temp
                temp += 1
        if a[0 + i][n - 1 - i] > 0:#proverka uglovyh znacheniy
            break
    for di in range(1 + i, n - 1 - i):#cycle pravoy stroki
        for dj in range(n - 1 - i, n - 2 - i, -1):
            while a[di][dj] == 0:
                a[di][dj] += temp
                temp += 1
        if a[n - 1 - i][n - 1 - i] > 0:#proverka uglovyh znacheniy
            break
    for di in range(n - 1 - i, -1 + i, -1):#cycle nignih strok
        for dj in range(n - 1 - i, -1 + i, -1):
            while a[di][dj] == 0:
                a[di][dj] += temp
                temp += 1
        if a[n - 1 - i][0 + i] > 0:#proverka uglovyh znacheniy
            break
    for di in range(n - 2 - i, 0 + i, -1):#cycle levyh strok
        for dj in range(1 + i):
            while a[di][dj] == 0:
                a[di][dj] += temp
                temp += 1
if n % 2 > 0:#zapolnenie centralnoy yacheiki
    a[k][k] = temp
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()