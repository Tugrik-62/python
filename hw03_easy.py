# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    tn = str (number)
    pl = '0.' + '0'*(ndigits-1) + '1'
    fpl = float(pl)
    i=tn.index('.')
    dig_len = i + ndigits
    dig = float(tn[:dig_len+1])
    if int(tn[dig_len:dig_len+1]) >= 5:
        dig = dig + fpl
    return dig


print(my_round(234.1234567, 5))
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    tn = str (ticket_number)
    a=0
    b=0
    for letter in tn[:3]:
       a += int (letter)

    for letter in tn[3:]:
        b += int (letter)
    if a == b:
        return 'Да'
    else:
        return 'Нет'

print(lucky_ticket(123006))
print(lucky_ticket(123211))
print(lucky_ticket(436751))



