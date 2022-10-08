print('Введите координаты точки А:')
xa = float(input('X: '))
ya = float(input('Y: '))
print("Введите координаты точки B:")
xb = float(input('X: '))
yb = float(input('Y: '))
from math import sqrt
print('Расстояние между A и B: ',round(sqrt((xa - xb)**2 + (ya - yb)**2), 3))