#счет количество символов умноженное на 100
a = str(input())
print((a.count('c') + a.count('g') + a.count('C') + a.count('G')) / (a.count('') - 1) * 100)
