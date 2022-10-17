# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

k = int(input('Введите число: '))
fibosub = [1,-1]
fibon = [1,1]
for i in range(2,k):
    list = fibon[i-1]+fibon[i-2]
    fibon.append(list)
    sub = fibosub[i-2] - fibosub[i-1]
    fibosub.append(sub)
fibosub.reverse()
fibosub.append(0)
print(f' for k = {k} =>{fibosub+fibon}')
