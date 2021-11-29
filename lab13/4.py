print ('Введите вещественное число')
A=float(input())
print ('Введите целое число, большее 0')
N=int(input())
p=1
for i in range (1, N+1):
    p=p+A**i
print (p)
