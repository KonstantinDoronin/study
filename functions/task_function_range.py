#функция range в зависимости от напрвления движения (+ или - шаг)
def my_range(start, stop, step=1):#sozdaem funkciyu range, step zadaem po umolchaniu - 1
    res = []#pustoy spisok dlya nakoplenya elementov
    if step > 0:# na uvelichenie
        x = start
        while x  < stop:
            res += [x]#nakoplenie znacheniiy v spiske
            x += step
    elif step < 0:# na umensheniye
        x = start
        while x > stop:
            res += [x]
            x += step
    return res
print(my_range(15, 2, -3))
print(my_range(stop=20, start=10))#mogno ukazat chto est chto