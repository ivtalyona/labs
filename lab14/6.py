print ('Введите целое число, большее 1')
N = int (input())
k=2
a=1
b=1
s=0
while s<=N:
    s=a+b
    a=b
    b=s
    k=k+1
print(k)