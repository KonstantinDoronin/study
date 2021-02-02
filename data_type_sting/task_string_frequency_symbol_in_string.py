#считает количество символов "С" в строке
a = str(input())
cnt = 0
for symb in a:
    if symb == 'C':
        cnt += 1
print(cnt)
