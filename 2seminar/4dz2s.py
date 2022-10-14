# Задайте список из n элементов, заполненных числами из промежутка [-n, n]. Найдите 
# произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в 
# одной строке одно число

from random import Random, randint


n = int(input('Введите число :'))
numbers = []
for i in range(n):
    numbers.append(randint(-n,n+1))
    
print(numbers)
