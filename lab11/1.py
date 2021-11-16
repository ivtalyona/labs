print ('введите А')
A = int ( input())
print ('введите В')
B = int ( input())
if A!=B:
    if A>B:
        B=A
    else:
        A=B
else:
    A=0
    B=0
print ('A=', A, 'B=', B)
