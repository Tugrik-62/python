# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def create (Name):
    dir_path = os.path.join(os.getcwd(), str(Name))
    try:
        os.mkdir(dir_path)
        print('Успешно создано')
    except FileExistsError:
        print ('Невозможно создать. Такая директория уже существует')

def delete (Name):
    dir_path = os.path.join(os.getcwd(), str(Name))
    try:
        os.rmdir(dir_path)
        print('Успешно удалено')
    except FileNotFoundError:
        print ('Невозможно удалить. Такая директория НЕ существует')

if __name__ == "__main__":
    
    for n in range(1,10):
        Name = 'dir_' + str(n)
        create(Name)

    for n in range(1,10):
        Name = 'dir_' + str(n)
        delete(Name)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def getList():
    files = os.listdir(path=os.getcwd())
    print('Содержание текущей папки: ')
    for i in files:
        print(i)

def goDir(Name):
    try:
        os.chdir(Name)
        print('Успешно перешел')
    except FileNotFoundError:
        print ('Невозможно перейти. Такая директория НЕ существует')

if __name__ == "__main__":  
    getList()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys

def copyCurrent():
    Name = os.path.basename(__file__)
    f_fr = open(Name, 'tr', encoding='utf-8')
    stroka = f_fr.read()
    f_fr.close()
    f_to = open('Copy_of_' + Name, 'tw', encoding='utf-8')
    f_to.write(stroka)
    f_to.close()

if __name__ == "__main__":
    copyCurrent()
