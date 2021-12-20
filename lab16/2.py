print ('Введите целое число N, большее 1')
N=int (input())
print ('Введите первый член А геометрической прогрессии')
A=int (input())
print ('Введите знаменатель D')
D=int (input())
a=[0]*N
a[0]=A
i=int
for i in range (0, N-1):
    a[i+1]=a[i]*D

print(' '.join(map(str, a)))
