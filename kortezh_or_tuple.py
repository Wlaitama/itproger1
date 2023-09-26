# Кортеж - это списки, которые мы заполняем и не можем их в дальнейшем изменять
data = (3, 4, True, "Hello")  # Разница между списками это скобки () [] либо без скобок вообще
print(data.count(4))
print("-----------------")
for i in data:
    print(i)

nums = [5, 7, 8]  #Переделываю список в кортеж
new_nums = tuple(nums)
print(new_nums)

word = tuple("Hello world")
print(word)