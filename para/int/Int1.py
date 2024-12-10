def one1():
    print("Составить программу, которая получив целое десятичное число и основание некоторой ПСС, выводит цифры записи этого числа в этой ПСС.")
    n = int(input("Введите число: "))
    c= int(input("Введите систему 2-16: "))
    b = '0123456789ABCDEF'
    d=""
    if c<=16 and c>1:
        while n > 0:
            d=b[n%c]+d # Запись остатка от деления в переменную
            n = n // c # Целочисленное деление числа для продолжения цикла
    else:
        print("Неподходящая степень счисления")
    print(d) # Ввывод числа


def one2():
    print("Составить программу, которая получает цифры записи целого числа в некоторой ПСС и основание этой ПСС выдает десятичную форму числа.")
    n = str(input("Введите число: "))
    c= int(input("Введите систему 2-16: "))
    d = '0123456789ABCDEF'
    b=0 # переменная результата
    count=0 # Переменная для степени
    for i in range(1,len(n)+1): #Цикл для перевода числа в 10 систему счисления
        b+=d.index(n[-i])*c**count
        count+=1
    print(b)



def one3():
    print("Перевести целое число из ПСС с одним основанием в ПСС с другим основанием")
    n = str(input("Введите число: "))
    c= int(input("Введите систему: "))
    a= int(input("Введите систему в которую надо перевести: "))
    b=0
    s=""
    d = '0123456789ABCDEF'
    count=0
    for i in range(1,len(n)+1): #Цикл для перевода числа в 10 систему счисления
        b+=d.index(n[-i])*c**count #Присвоения значения для перевода в 10 степень
        count+=1
    while b!=0: #Перевод из 10 в заданную степень
        s+=str(b%a) #Процесс переноса
        b//=a
    print(s[::-1]) #Вывод значения


def one4():
    print("Составьте программу, выводящую на экран таблицу умножения для указанной ПСС.")
    d = '0123456789ABCDEF'
    count=int(input("Введите систему счисления 2-16: "))
    
    if count>=2 and count<=16: #Проверка системы счисления    
        for i in range(0,count): #Цикл для первого значения в таблицу
            print()
            for j in range(0,count): #Цикл для второго значения в таблице
                print(d[i],"*",d[j],"=",i*j) #Вывод таблицы умножения
    else:
        print("Неверная степень счисления") #Вывод при ошибке


def one5():
    print("Получить запись правильной десятичной дроби в некоторой ПСС. ")
    n=float(input("Введите число: "))
    c=int(input("Введите систему: "))
    d = '0123456789ABCDEF'
    back=n%1 # Числа после запятой
    one=''
    b=''
    while n > 0:
        n=int(n//1)
        b += d[n % c] # Запись остатка от деления в переменную
        n = n // c # Целочисленное деление числа для продолжения цикла


    for i in range(10): #перевод чесел после запятой до 10
        back*=c
        if back>=1: #Проверка числа
            one=d[int(back//1)]+one #Запись числа в переменную
            back=back-back//1
        else:
            one+=str(0)
    print(b[::-1],'.',one[::-1],sep='') #Вывод результата

def one6():
    print("Правильную дробь, записанную в некоторой ПСС, преобразовать в десятичную запись.")
    n=float(input("Введите число: "))
    c=int(input("Введите систему: "))
    d = '0123456789ABCDEF'
    back=n%1 # Числа после запятой
    one=''

    for i in range(10): #перевод чесел после запятой до 10
        back*=c
        if back>=1: #Проверка числа
            one=d[int(back//1)]+one #Запись числа в переменную
            back=back-back//1
        else:
            one+=str(0)
    print('0.',one[::-1],sep='') #Вывод результата
    print(one)



def two2(): 
    print("Есть набор цифр числа. Сосчитать само число.")
    a=str(input("Введите набор чисел: ")) # Введение набора чисел
    a=a.replace(" ","") # Удаление всех пробелов
    b=0
    for i in range(len(a)):
        b=int(a[i])+b # Суммирование цифр из набора
    print(b)


def two3():
    print("Не используя приемов обработки строковой информации выяснить является ли число палиндромом?")
    a=str(input("Введите число: "))
    if a==a[::-1]: # Ввывод числа наоборот
        print("Число палиндром")
    else:
        print("Число не палиндром")


def third1():
    print("Составить (получить на экране) таблицу Пифагора для логических операций AND , OR , XOR , IMP , NOT .")
    values = [False, True]

    # Заголовок таблицы
    print("| A     | B     | A AND B |")
    print("|-------|-------|---------|")

    # Заполняем таблицу
    for A in values:
        for B in values:
            result = A and B  # Выполняем логическую операцию AND
            print(f"| {A:<5} | {B:<5} | {result:<7} |")
    # Таблица OR
    print("Таблица истинности для A OR B:")
    print("| A     | B     | A OR B |")
    print("|-------|-------|--------|")
    for A in values:
        for B in values:
            result = A or B  # Выполняем операцию OR
            print(f"| {A:<5} | {B:<5} | {result:<6} |")
    print()

    # Таблица XOR
    print("Таблица истинности для A XOR B:")
    print("| A     | B     | A XOR B |")
    print("|-------|-------|---------|")
    for A in values:
        for B in values:
            result = A ^ B  # Выполняем операцию XOR
            print(f"| {A:<5} | {B:<5} | {result:<7} |")
    print()

    # Таблица IMP
    print("Таблица истинности для A IMP B:")
    print("| A     | B     | A IMP B |")
    print("|-------|-------|---------|")
    for A in values:
        for B in values:
            result = not A or B  # Выполняем операцию IMP
            print(f"| {A:<5} | {B:<5} | {result:<7} |")
    print()

    # Таблица NOT
    print("Таблица истинности для NOT A:")
    print("| A     | NOT A |")
    print("|-------|-------|")
    for A in values:
        result = not A  # Выполняем операцию NOT
        print(f"| {A:<5} | {result:<5} |")




def third3():
    print("Существуют ли числа a и b такие, что  a and b = (a+b)/2")
    n,c=int(input("Введите число: ")),int(input("Введите число: "))
    if n and c == (n+c)/2: 
        print("Не может быть такой пары как",n,"и",c) # Если условие не верно
    else:
        print("Такая пара может быть") # Если условие верно




def four4():
    print("Существуют ли числа a и b такие, что  a or b = (a+b)/2")
    n,c=int(input("Введите число: ")),int(input("Введите число: "))
    if n or c == (n+c)/2: 
        print("Не может быть такой пары как",n,"и",c) # Если условие не верно
    else:
        print("Такая пара может быть") # Если условие верно
