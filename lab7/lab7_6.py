print ('Введите значение коэффициента А1')
A1=int(input())
print ('Введите значение коэффициента В1')
B1=int(input())
print ('Введите значение коэффициента С1')
C1=int(input())
print ('Введите значение коэффициента А2')
A2=int(input())
print ('Введите значение коэффициента В2')
B2=int(input())
print ('Введите значение коэффициента С2')
C2=int(input())
x=float()
y=float()

 
x= (-(C2*B1)+(B2*C1))/(-(B1*A2)+(A1*B2));
y=(C1-(A1*x))/B1


print ('Решением системы являетя x=',x,'y=',y)
