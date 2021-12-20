def Sign (x:float):
    if x<0:
        return-1
    if x==0:
        return 0
    if x>0:
        return 1

print ('Введите число А')
A=float (input())
print ('Введите число В')
B=float (input())
s=Sign(A)+Sign(B)
print(s)