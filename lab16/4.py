print ('Введите число N')
N=int(input())
a=[0]*N
for i in range (N):
    a[i]=int (input())
for i in range (0, N//2):
    print (a[i], a[N-i-1])
if N%2!=0:
    print (a[N//2])