print ('Введите целое число N, большее 0')
N=int (input())
a=[0]*N
i=int
a[0]=1
for i in range (0, N-1):
    a[i+1]=a[i]+2

print(' '.join(map(str, a)))