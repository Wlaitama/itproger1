import datetime as d, sys, os, time, platform  # модули ищем в официальном сайте
from math import sqrt as s, ceil
time.sleep(1)
print("Hello world!")

print(d.datetime.now().time().hour)

print(os.name)

print(platform.uname())
print(platform.system())

print(ceil(s(25)))
print("---------------------")
import my_module as my

print(my.name)
my.hello()
print(my.summa_three(5, 3, 2))