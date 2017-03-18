def ger_sqrt(num):
    x = 1
    sq = False
    while sq == False:
        pre = x
        x = 0.5 * (x + num / x)
        if  x ** 2 == num or x == pre:
            sq = True
    return x;
import math
print('введите число')
num = int(input())
x = ger_sqrt(num)
print('мой код ', x)
print('выстоенная функция sqrt', math.sqrt(num))
