print ('Введите четырехзначное число')
A = int (input ())
a = A // 1000
b = (A // 100) % 10
c = (A // 10) % 10
d = A % 10
H = d*1000 + c*100 + b*10 + a
j = (A==H)
print ('Данное число читается одинаково слева направо и справа налево =', j)
