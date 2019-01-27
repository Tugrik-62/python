# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import hw05_easy as easy

while True:
    print('Выберите действие: ')
    print('1. Перейти в папку: ')
    print('2. Просмотреть содержимое текущей папки: ')
    print('3. Удалить папку: ')
    print('4. Создать папку: ')
    print('5. Выйти и закончить: ')
    a = input()
    if a == '1':
        name = input('Укажите название папки: ')
        easy.goDir(name)
    if a == '2':
        easy.getList()
    if a == '3':
        name = input('Укажите название папки: ')
        easy.delete(name)
    if a == '4':
        name = input('Укажите название папки: ')
        easy.create(name)
    if a == '5':
        break


        
