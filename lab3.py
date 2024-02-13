import math

# Задача 1
def task1(a):
    return 4 * a

# Задача 2
def task2(a):
    return a ** 2

# Задача 3
def task3(a, b):
    area = a * b
    perimeter = 2 * (a + b)
    return area, perimeter

# Задача 4
def task4(d):
    return math.pi * d

# Задача 5
def task5(a):
    volume = a ** 3
    surface_area = 6 * a ** 2
    return volume, surface_area

# Задача 6
def task6(a, b, c):
    volume = a * b * c
    surface_area = 2 * (a*b + b*c + a*c)
    return volume, surface_area

# Задача 7
def task7(radius):
    length = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return length, area

# Задача 8
def task8(a, b):
    return (a + b) / 2

# Задача 9
def task9(a, b):
    return math.sqrt(a * b)

# Задача 10
def task10(x, y):
    sum_squares = x**2 + y**2
    difference_squares = x**2 - y**2
    product_squares = x**2 * y**2
    quotient_squares = x**2 / y**2
    return sum_squares, difference_squares, product_squares, quotient_squares

# Задача 11
def task11(a, b):
    sum = abs(a) + abs(b)
    difference = abs(a) - abs(b)
    product = abs(a) * abs(b)
    if b != 0:
        quotient = abs(a) / abs(b)
    else:
        quotient = None
    return sum, difference, product, quotient

# Задача 12
def task12(a, b):
    c = math.sqrt(a**2 + b**2)
    perimeter = a + b + c
    return c, perimeter

# Задача 13
def task13(R1, R2):
    S1 = math.pi * R1**2
    S2 = math.pi * R2**2
    S3 = S1 - S2
    return S1, S2, S3

# Задача 14
def task14(L):
    R = L / (2 * math.pi)
    S = math.pi * R**2
    return R, S

# Задача 15
def task15(S):
    R = math.sqrt(S / math.pi)
    D = 2 * R
    L = 2 * math.pi * R
    return D, L

# Задача 16
def task16(x1, x2):
    return abs(x2 - x1)

# Задача 17
def task17(a, b, c):
    AC = abs(c - a)
    BC = abs(c - b)
    return AC, BC, AC + BC

# Задача 18
def task18(a, b, c):
    AC = abs(c - a)
    BC = abs(c - b)
    return AC * BC

# Задача 19
def task19(x1, y1, x2, y2):
    length = abs(x2 - x1)
    width = abs(y2 - y1)
    perimeter = 2 * (length + width)
    area = length * width
    return perimeter, area

# Задача 20
def task20(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

a = 2
b = 3
c = 4
d = 5
radius = 6
x = 7
y = 8

print("Периметр квадрата:", task1(a))
print("Площадь квадрата:", task2(a))
print("Площадь и периметр прямоугольника:", task3(a, b))
print("Длина окружности:", task4(d))
print("Объем и площадь поверхности куба:", task5(a))
print("Объем и площадь поверхности параллелепипеда:", task6(a, b, c))
print("Длина окружности и площадь круга:", task7(radius))
print("Среднее арифметическое двух чисел:", task8(a, b))
print("Среднее арифметическое корней из двух чисел:", task9(a, b))
print("Операции над квадратами двух чисел:", task10(x, y))
print("Задача 11:", task11(a, b))
print("Задача 12:", task12(a, b))

R1 = 5
R2 = 3
print("Задача 13:", task13(R1, R2))

L = 20
print("Задача 14:", task14(L))

S = 50
print("Задача 15:", task15(S))

x1 = 3
x2 = 8
print("Задача 16:", task16(x1, x2))
print("Задача 17:", task17(a, b, c))
print("Задача 18:", task18(a, b, c))

x1 = 2
y1 = 4
x2 = 7
y2 = 9
print("Задача 19:", task19(x1, y1, x2, y2))

x1 = 1
y1 = 2
x2 = 4
y2 = 6
print("Задача 20:", task20(x1, y1, x2, y2))
