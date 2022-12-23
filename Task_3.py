# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# (1, 1*2, 1*2*3, 1*2*3*4) и т.д
# 4 -> [ 1, 2, 6, 24 ]
# 6 -> [ 1, 2, 6, 24, 120, 720 ]


from math import factorial
n = int(input('Введите число: '))
print(list(map(lambda x: ((x == 1) and 1) or x * factorial(x -1),list(range(1,n+1)))))