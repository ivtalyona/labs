print ('Введите число а')
a = int (input ())
print ('Введите число b')
b = int (input ())
print ('Введите число c')
c = int (input ())
d = ((a+b) > c) and ((c+b) > a) and ((a+c) > b)
print ('Существует треугольник со сторонами a, b, c =', d)
