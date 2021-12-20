def RingS (R1: float, R2:float):
    return 3.14*((R2-R1)**2)
for i in range (3):
    print ('Введите внутренний радиус R1')
    R1=float(input())
    print ('Введите внешний радиус R2')
    R2=float(input())
    s=RingS(R1,R2)
    print (s)