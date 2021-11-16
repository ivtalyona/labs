print ('введите А')
A = int ( input())
print ('введите В')
B = int ( input())
print ('введите C')
C = int ( input())
if (A<B) and (A<C):
    s=B+C 
if (A>C) and (B>C):
    s=A+B
if (B<A) and (B<C):
    s= A+C
print('Сумма двух наибольших чисел =',s)
