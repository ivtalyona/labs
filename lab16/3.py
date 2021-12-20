print ('Введите целое число N, большее 2')
N=int (input())
print ('Введите целое число А')
A=int (input())
print ('Введите целое число В')
B=int (input())
a=[0]*N
a[0]=A
a[1]=B
i=int
s=a[0]
for i in range (2, N):
    s=s+a[i-1]
    a[i]=s
print(' '.join(map(str, a)))
