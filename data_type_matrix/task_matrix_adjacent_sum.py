#создание матрицы, состоящий из суммы рядом стоящих элементов начальной матрицы
a = [i for i in input().split()]#ввод строк матрицы
b = []
row = 0
col = 0
sum = 0
while a != ['end']:#ввод до тех пор, пока не ввели "end"
    b.append([int(i) for i in a])
    row += 1#считаем количество столбцов в матрице
    col = len(a)#считаем количество строк (так как она или квадратная или прямоугольная)
    a = [i for i in input().split()]#ввод новой строки
for i in range(row):#большой цикл для каждого элемента (перебор по row и col)
    for j in range(col):
        if row == 1 and col == 1:#если единичная матрица
            sum = 4 * b[i][j]
            print(sum)
            break
        if i + 1 < row and j + 1 < col:#для не угловых элементов матрицы
            sum = b[i - 1][j] + b[i + 1][j] + b[i][j - 1] + b[i][j + 1]
            print(sum, end='\t')
        if i + 1 == row and j + 1 == col:#для правого нижнего элемента матрицы
            sum = b[i - 1][j] + b[i][j - 1] + b[0][j] + b[i][0]
            print(sum)
        if i + 1 == row and j + 1 < col:#боковые элементы по строке
            sum = b[i][j + 1] + b[i][j - 1] + b[i - 1][j] + b[0][j]
            print(sum, end='\t')
        if i + 1 < row and j + 1 == col:#боеоквые элементы по столбцу
            sum = b[i][j - 1] + b[i][0] + b[i + 1][j] + b[i - 1][j]
            print(sum, end='\n')