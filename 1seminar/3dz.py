x = int(input('Введите x: '))
y = int(input('Введите y: '))
if x == 0 or y == 0:
    print('Попробуйте снова')
if x > 0 and y > 0:
    print('1')
if x < 0 and y > 0:
    print('2')
if x < 0 and y < 0:
    print('3')
if x > 0 and y < 0:
    print('4')