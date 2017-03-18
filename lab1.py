print('+ сложение\n- вычитание\n* умножение\n/ деление\n** возведение в степень\n// нахождение корня\nmew начать вычисления сначла\nexit выход')
print('введите число')
a = int(input())
print('введите операцию')
zn = input()
while (zn != 'exit'):
    if zn == 'new':
        print('введите число')
        a = int(input())
        print('введите операцию')
        zn = input()
    print('введите число')
    b=int(input())
    if zn == '+':
        a = a + b
    elif zn == '-':
        a = a - b
    elif zn == '*':
        a = a * b
    elif zn == '/':
        a = a / b
    elif zn == '**':
        a = a ** b
    elif zn == '//':
        a = a ** ( 1 / b )
    print('ответ ', + a)
    print('введите операцию')
    zn = input()

