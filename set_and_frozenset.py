#data = set('hello')
data_1 = {5, 7, 6, 4}   # Так же как и словарь, только в словаре идет сначало индекс, а потом значение через :

data_1.add(32)
print(data_1)
data_1.update([32, 4, True])
print(data_1)
data_1.remove(True)
print(data_1)
data_1.pop()
print(data_1)
print('-----------------')

nums = [5, 7, 5, 5, 4]
new_nems = set(nums)
print(new_nems)
print('-----------------')

new_data = frozenset([3, 5, True, "Hello"])  #Наподобие кортежа и set (не изменяется)
print(new_data)

#data_1.clear()
#print(data_1)