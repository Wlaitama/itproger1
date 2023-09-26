nums = [5, 7, 4, 2, True, "user", [6, 2]]

nums[0] = 50

print(nums)
print(nums[-1][1])

nums.append(100)
print(nums)

nums.insert(1, 10)
print(nums)

b = (5, 7, 78)
nums.extend(b)
nums.remove("user")  # удялет определенный элемент
nums.remove([6, 2])
nums.sort()
nums.pop()  # удаляет посл элемент, в () можно указать индекс
print(nums)
print("Кол-во 7: ", nums.count(7))
print(len(nums))

for i in nums:
    i *= 1
    print("\n", i)

  # Создание цикла
n = int(input("Enter length list: "))
us = []
a = 0

while a < n:
    string = "Enter element №" + str(a+1) + ": "
    us.append(input(string))
    a += 1

print(us)