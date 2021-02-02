#sortirovka 3 chisel - max - min - ostatok

a = int(input())
b = int(input())
c = int(input())
if (c <= a >= b and b >= c):
    print(str(a) + '\n' + str(c) + '\n' + str(b))
elif (c <= a >= b and b <= c):
    print(str(a) + '\n' + str(b) + '\n' + str(c))
elif (a <= b >= c and a >= c):
    print(str(b) + '\n' + str(c) + '\n' + str(a))
elif (a <= b >= c and c >= a):
    print(str(b) + '\n' + str(a) + '\n' + str(c))
elif (b <= c >= a and a >= b):
    print(str(c) + '\n' + str(b) + '\n' + str(a))
elif (b <=c >= a and b >= a):
    print(str(c) + '\n' + str(a) + '\n' + str(b))
else:
    print('Parabellum')