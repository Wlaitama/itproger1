word = 'itproger'
print(word[1])
print(len(word))
print(word.count('r'))
print(word.upper())
print(word.islower())  # Проверяет строку на строчное провописание (is)
print(word.lower())
print(word.capitalize())  # 1 букву заглавной
print(word.find('p'))  # Находит какой инекс найденный символ
print("--------------------------")

print(word[0:4])  # С какого индекс и до какого
print(word[4:])
print(word[1:-1:2])
print("--------------------------")

wordes = "Footbal, basketball, tennis"
print(wordes.split(', '))  # Разбивать символами между словами
hobby = wordes.split(', ')
print(hobby[1])

for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()

print(hobby)
print("--------------------------")

result = ', '.join(hobby)

print("\nКорректно и красиво выведено: ",result)
print("--------------------------")

lis = [6, 4, 'Stroka', True, 6.5]
print(lis[2:5])
print(lis[2:5:2])
print(lis[::])
print(lis[::-1])
