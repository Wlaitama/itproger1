def test(word):
    print(word, end="")
    print("!")

test("Hi")
test(56)
print("-----------------------")
def summa(a, b):
    return a+b


res = summa(3, 5.6)
print(res)
print(summa("H", "i"))
print("-----------------------")


def minimal(el):
    mini = el[0]
    for i in el:
        if i < mini:
            mini = i
    return mini

num1 = [5, 4, 7, 9, 6]
minimal(num1)

num2 = [3.4, 4.6, 7.9, 9.2, 6.1]
minimal(num2)

if minimal(num1)<minimal(num2):
    print("Самый минимальный: ", minimal(num1))
else:
    print("Самый минимальный: ", minimal(num2))

print("----------------------")

func_2 = lambda x, y: x*y
resa = func_2(3, 56)
print(resa)