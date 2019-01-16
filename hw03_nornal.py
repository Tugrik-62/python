# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def f(n):
    if n<3:
        return 1
    return f(n-1) + f(n-2)

def fibonacci(n, m):
    a = []
    for i in range(n, m):
        a.append(f(i))
    return a

print (fibonacci(1,15))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    i = len(origin_list)
    while i > 1:
        for j in range(i - 1):
            if origin_list[j] > origin_list[j + 1]:
                a = origin_list[j]
                origin_list[j] = origin_list[j+1] 
                origin_list[j+1] = a
                
        i -= 1
    return origin_list    

print( sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

t=0.0001

def seredina (a=[1], b=[1]):
    g=[0,1]
    g[0] = (a[0]+b[0])/2
    g[1] = (a[1]+b[1])/2
    return g

A = [1,5]
B = [5,4]
C = [6,0]
D = [2,1]

def isParallelogramm(A=[1],B=[1],C=[1],D=[1]):
    AC = seredina (A,C)
    BD = seredina (B,D)
    if abs(AC[0] - BD[0]) < t and abs(AC[1] - BD[1]) < t:
        return 'Это параллелограмм'
    else:
        return 'Это НЕ параллелограмм'

    
print (A,B,C,D)
print (isParallelogramm(A,B,C,D))
C = [6,1]
print (A,B,C,D)
print (isParallelogramm(A,B,C,D))

