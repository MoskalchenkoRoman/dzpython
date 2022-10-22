# Вычислить число c заданной точностью d

import math

pi = math.pi
print('ПИ = ', pi)
# d = 0.001
d = float(input('Введите число в формате 0,00...1 :'))
print(f'Точность = {d}')
count = 0
while d < 1:
    count += 1
    d = d*10
print(round(pi, count))
