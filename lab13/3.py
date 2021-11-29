print ('Введите целое число, большее 0')
N=int(input())
p=0
for i in range (1, N+1):
    p=p+(i*2-1)
    print (p)
print ('Квадрат числа =', p)