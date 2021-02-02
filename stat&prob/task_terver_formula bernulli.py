#число испытаний
k = 30
pp = 2/3
#число благоприятных исходов
j = 10
p = 1/3
def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n
m = fac(k)/(fac(j) * fac(k - j)) * p ** (j) * pp ** (k-j)
print(m)
