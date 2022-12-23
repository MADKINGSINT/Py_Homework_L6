# Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел.
# Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел.
# Ввод чисел продолжается до ввода пустой строки.
# Входные данные Выходные данные
# 36 6
# 12
# 144
# 18
l = []
from functools import reduce
import math
sp = []
while True:

    st = (input('Введите число:     '))
    if st == '':

        break
    else:
        l.append(int(st))

res_sp = []
spis = []
def find_gcd(x, y):
	
	while(y):
		x, y = y, x % y
	
	return x
		



num1 = l[0]
num2 = l[1]
gcd = find_gcd(num1, num2)

for i in range(2, len(l)):
	gcd = find_gcd(gcd, l[i])
	
print(gcd)






