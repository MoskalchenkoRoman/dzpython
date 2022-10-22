# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
list = [random.randint(0,6) for i in range (10)]
print(list)
new_list = []
for char in list:
    if list.count(char) < 2:
        new_list.append(char)
print(new_list)