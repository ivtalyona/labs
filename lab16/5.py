print ('Введите число N')
N=int(input())
a=[0]*N
for i in range (N):
    a[i]=int (input())
for i in range (0,N,2):
    print(a[i])
b=a[::-1]
if N%2==0:
    for i in range (0,N,2):
        print (b[i])
else:
    for i in range (1,N,2):
        print (b[i])
    
    