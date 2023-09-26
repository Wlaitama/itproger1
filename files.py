data = input("Введите текст: ")

file = open('files/text.txt', 'w')  #Если этого файла нету, создается автоматически 'w'-write, 'a'-append, 'r'-read

file.write("Hello")
file.write("!!!\n")
file.write("New stroka\n")
file.write(data + "\n")

file.close()  # обязательно закрывать, будет утечка данных

file_new = open('files/text.txt', 'r')

#print(file_new.read())
#print(file_new.read(5))  # сколько символов вывидено

for line in file_new:
    print(line, end="")

file_new.close()
