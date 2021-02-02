#poiks n-go znacheniya chisla fibonachi

n = int(input())#kakoye po poraydku chislo fibonachi nam nado naity ?
a = 0
b = 1
for i in range(n):#recursivniy cycle
    c = a + b#FN=N-1 + N - 2
    a = c
    b = c - b
print(c)