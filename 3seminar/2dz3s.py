# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент,
#  второй и предпоследний и т.д.

list = [1, 2, 3, 4, 5, 6]
list2 = []
last = len(list)   
for i in range(len(list)):
    while i < len(list)/2 and last > len(list)/2:
        last = last - 1
        a = list[i] * list[last]
        list2.append(a)
        i += 1
print(list2)

