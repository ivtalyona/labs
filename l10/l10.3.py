print ('Введите число А')
A = int ( input ())
d = (A // 100 == 0) and (A % 2 == 0)
print ('Данное число является четным двузначным =', d)
