x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
x3=int(input())
y3=int(input())
a=((x1-x2)**2+(y1-y2)**2)**0.5
b=((x2-x3)**2+(y2-y3)**2)**0.5
c=((x1-x3)**2+(y1-y3)**2)**0.5
P=a+b+c
g=P/2
S=(g*(g-a)*(g-b)*(g-c))**0.5
print("периметр =", P, "Площадь =", S)
