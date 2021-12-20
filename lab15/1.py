def PowerA3(A:float, B:float):
    B=A*A*A
    return (B)
for i in range (5):
    print ('Введите число')
    A=float(input())
    B = PowerA3 (A,1)
    print (B)


