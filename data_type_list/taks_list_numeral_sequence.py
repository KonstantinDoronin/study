#sozdaniya posledovatelnosty chisel, ravnoy vvedennomu chislu n , vnutri kotorogo kol-vo
#elementov ravno svoyemu znacheniyu

n = int(input())#input number
b = []#create empty list
count = 0#create
for i in range(n):#cycle for making list from 1 to n with step 1
    a = [int(i + 1) for i in range(n)]#creating list
    while b.count(a[i]) != i + 1 and len(b) != n:#count quantaty numbers, compare in with index and rule -len not more n
       b.append(a[i])#add symbol in b
for i in b:# convert list in continuously int
    print(i, end=' ')
