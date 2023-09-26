class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name=None, age=None, isHappy=None):  # конструктор
        # self.name = name #можно вручную писать
        # self.age = age
        # self.isHappy = isHappy
        self.set_data(name, age, isHappy)  # Можно обратиться к функциям
        self.set_print()

    def set_data(self, name=None, age=None, isHappy=None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def set_print(self):
        print("Name: ", self.name, "; Age: ", self.age, "; Happy: ", self.isHappy)


cat1 = Cat("Barsik", 3, True)  # С помощью конструктора

# cat1.set_data("Barsik", 3, True)  #С помощью функции(метода)

cat2 = Cat("Murka", 2)

# cat2.name = "Murka"  # без помощи function
# cat2.age = 2
# cat2.isHappy = False
print("--------------------")
cat1.set_print()
print(cat2.name)
