try:
    # Нужен для закрытия файла, даже если выбивает ошибку и открывает файл заново!
    with open('text.txt', 'r', encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("Файл не найден!")