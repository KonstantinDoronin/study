def update_dictionary(d, key, value): #функция списка d
    if key in d: #если ключ есть уже в словаре d  -  добавляем значение к списку значений
        d[key] += [value]
        return#дабы не было повторных сравнений - каждый if заканчиваем return
    if key not in d:#если ключ нет в словаре
        temp_key = 2 * key
        if temp_key not in d:#если ключ * 2 не в списке, вносим в словарь key-value
            d[temp_key] = [value]
            return
        if temp_key in d:#если ключ  * 2 есть в списке  - добавляем значение к списку значений
            d[temp_key] += [value]
            return
d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 3, -3)
print(d)                            # {2: [-1, -2, -3]}