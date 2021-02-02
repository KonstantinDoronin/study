#игра сапер


n, m, k = (int(i) for i in input().split()) #row, col and mines
a = [[0 for j in range(m)] for i in range(n)] #create empty table
# mines in table
for i in range(k): #mines value
    row, col = (int(i) - 1 for i in input().split()) #zapisivayem row and column every mines
    a[row][col] = -1 #write mine with coordinate row, col
#mines search
for i in range(n): #search in row
    for j in range(m): #search in column
        if a[i][j] == 0: #mine cell
            for di in range(-1, 2): #seach in near row ( -1 0 1)
                for dj in range(-1, 2): #search in near column (-1 0 1)
                    ai = i + di #coordinate by row
                    aj = j + dj #coordinate by column
                    # (ai, aj)
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1: #check nearest mine
                        a[i][j] += 1
#output tables with mines
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end='')
        elif a[i][j] == 0:
            print('.', end='')
        else:
            print(a[i][j], end='')
    print()
for i in range(n):
    print(a[i])