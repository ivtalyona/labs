def Quarter (x: float, y:float):
    if x>0:
        if y>0:
            return 1
        else:
            return 4
    else:
        if y>0:
            return 2
        else: 
            return 3
for i in range (3):
    print ('Введите ненулевую x-координату')
    x=float(input())
    print ('Введите ненулевую у-коoрдинату')
    y=float(input())
    s=Quarter(x,y)
    print ('Номер координатной четверти:', s)
