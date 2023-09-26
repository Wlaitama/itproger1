class Build:
    __year = None  # Инкапсуляция - защита данных, создана для того, чтобы мы не изменяли данных, которые были уже заданы
    city = None



    def __init__(self,year,city):
        self.year = year
        self.city = city

    def get_info (self):
        print("Year: ", self.year, "City: ", self.city)

class School(Build):
    student = 0

    def __init__(self,student,year,city):
        super(School,self).__init__(year,city)  #Super - это значит мы ссылаемся к первому(Основному) классу
        self.student = student

    def get_info(self):  #Полиморфизм - обращаемся к основному классу и ее методу, а потом переделываем
        super(School,self).get_info()
        print("Student: ", self.student)
class House(Build):
    pass
class Shop (Build):
    pass

school = School(100,2000, 'Grodno')
school.get_info()
house = House(3000, 'Brest')
shop = Shop(1000, 'Grodno')

