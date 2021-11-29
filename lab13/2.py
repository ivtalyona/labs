print ('Введите целое число, большее 0')
N=int(input())
p=1
for i in range (1, N+1):
    p=p*(i*0.1+1)
print (p)