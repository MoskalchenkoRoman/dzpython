day = int(input('введите номер дня недели: '))
if day > 7 or day < 1:
    print('Попробуйте еще раз')
elif day == 6 or day == 7:
    print('О да,Выходной!')
else:
    print('нееееет(идти на работу!')