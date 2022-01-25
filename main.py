import math

while True:
    a = int(input('Введите a:\n'))
    b = int(input('Введите b:\n'))
    c = int(input('Введите c:\n'))

    if a < 0:
        print ('Переменная "a" не может быть меньше нуля, введите заново:\n')
        a = int(input())

    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        xone = (-b - math.sqrt(discriminant)) / (2*a)
        xtwo = (-b + math.sqrt(discriminant)) / (2*a)
        print ('Первый корень: '+str(xone)+'\nВторой корень: '+str(xtwo))

    elif discriminant == 0:
        xone = -b / 2*a
        print('В данном уравнении только один корень, он равен: '+str(xone))

    elif discriminant <= 0:
        print ('Корней нет.')