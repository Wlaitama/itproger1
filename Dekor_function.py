# Для открытия нашего сайта в нашем браузере по умолчании
import webbrowser

def validator(func):
    def wrapper(url):
        if '.' in url:
            func(url)
        else:
            print("Неверный URL")
    return wrapper

@validator  #Декоратор - что-то на подобие проверки 
def open_url(url):
    webbrowser.open(url)

open_url("http://www.python.org")