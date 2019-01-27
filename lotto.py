"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""
import random
class Lotto:
    def __init__ (self):
        self.nabor = [i for i in range(1, 91)]
        self.meshok = []
        i = 0
        while i == 0:
            try:
                n = random.choice(self.nabor)
                self.meshok.append(n)
                self.nabor.remove(n)
            except IndexError:
                i = 1

    def showNabor(self):
        print ('В наборе: ', self.nabor)            

    def showMeshok(self):
        print ('В мешке остались боченки: ', self.meshok)

    def newStep(self):
        try:
            m = self.meshok.pop()
        except IndexError:
            print('Игра окончена')
            return 0
        return m        

class Igrok:
    def __init__ (self, Name):
        self.Name = Name
        self.card = []
        self.S1 = []
        self.S2 = []
        self.S3 = []

    def getName(self):
        return self.Name

    def genCard(self):
        i = 0
        while i < 15:
            k = random.randint (1, 91)
            if k not in self.card:
                self.card.append(k)
                i = i + 1
        self.S1 = [self.card[i] for i in range(0,15,3)]
        self.S2 = [self.card[i] for i in range(1,15,3)]
        self.S3 = [self.card[i] for i in range(2,15,3)]
        self.S1.sort()
        self.S2.sort()
        self.S3.sort()
        j=0
        while j < 4:
            n1 = random.randint (0, 9)
            self.S1.insert(n1, ' ')
            n2 = random.randint (0, 9)
            self.S2.insert(n2, ' ')
            n3 = random.randint (0, 9)
            self.S3.insert(n3, ' ')
            j = j + 1

    def showCard(self):
        
        print ('Карта игрока ', self.Name)
        print (' '.join(list(map(lambda x: str(x), self.S1))))
        print (' '.join(list(map(lambda x: str(x), self.S2))))
        print (' '.join(list(map(lambda x: str(x), self.S3))))
        
    def getStep(self, n):
        n = int(n)
        sch = 0
        if n in self.card:
            mm = self.card.index(n)
            self.card[mm] = '-'
            sch = self.card.count('-')
        if n in self.S1:
            m1 = self.S1.index(n)
            self.S1[m1] = '-'
            if sch < 15:
                return (1)
        if n in self.S2:
            m2 = self.S2.index(n)
            self.S2[m2] = '-'
            if sch < 15:
                return (1)
        if n in self.S3:
            m3 = self.S3.index(n)
            self.S3[m3] = '-'
            if sch < 15:
                return(1)
        if sch < 15:
            return (0)
        else:
            return (2)
                        
class Comp(Igrok):
    
    def putStep(self, k):
        k = int(k)
        y = self.getStep(k)
        return y

class Men(Igrok):
    
    def putStep(self, n):
        n = int(n)
        print('Вы можете:')
        print('1 - Зачеркнуть цифру')
        print('2 - Продолжить')
        ans = int(input())
        sch = 0
        if n in self.card:
            if ans == 2 :
                return 3
            mm = self.card.index(n)
            self.card[mm] = '-'
            sch = self.card.count('-')
        if n in self.S1:
            m1 = self.S1.index(n)
            self.S1[m1] = '-'
            if sch < 15:
                return (1)
        if n in self.S2:
            m2 = self.S2.index(n)
            self.S2[m2] = '-'
            if sch < 15:
                return (1)
        if n in self.S3:
            m3 = self.S3.index(n)
            self.S3[m3] = '-'
            if sch < 15:
                return(1)
        if sch < 15:
            if ans == 1 :
                return 3
            return (0)
        else:
            return (2)
        y = self.getStep(n)
        
        return y


L2 = Lotto()
F1 = Comp('Компьютер')
F1.genCard()
F2 = Men('Человек')
F2.genCard()
F1.showCard()
F2.showCard()
i = 0
while i<2:
    Num = L2.newStep()
    if Num == 0 :
        i = 2
        break
    print('Боченок: ', Num)
    N1 = F1.putStep(Num)
    N2 = F2.putStep(Num)
    F1.showCard()
    F2.showCard()
    if N1 == 2:
        print('Выиграл игрок ',  F1.getName())
        print('Игра окончена')
        i = 2
        break
    if N2 == 2:
        print('Выиграл игрок ', F2.getName())
        print('Игра окончена')
        i = 2
        break
    if N1 == 3:
        print('Игрок ',  F1.getName(), ' проиграл')
        print('Игра окончена')
        i = 2
        break
    if N2 == 3:
        print('Игрок ', F2.getName(), ' проиграл')
        print('Игра окончена')
        i = 2
        break
    i = 0    
    


            
        

        
        
