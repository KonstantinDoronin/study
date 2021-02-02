#fuknciya poiska minimuma iz spiska znacheniy


def min(*a):#sozdarm funkciu
    m = a[0]#v peremennuu m zapisyvaem znachenie pervogo elementa
    for i in a:#cycle sravneniya po vsem znacheniyam
        if m > i:
            m = i
    return m
print(min(12,5))#chto hotim sravnit