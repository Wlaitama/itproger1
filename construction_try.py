# Создание исключений

x=0

while x==0:
    try:
        x = int(input("Введите число: "))
        print(x)
        try:
            y = 100/x
        except ZeroDivisionError:
            print("100 на 0 не делиться!\n")
            print("Напиши заново!")
        else:
            print("Число: ", y)
    except ValueError:
        print("Введите именно число!")
    else:
        print("Молодец)")
    finally:
        print("Finally")