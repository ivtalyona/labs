print ('Введите количество процентов Р, меньшее 25, большее 0')
P= float(input())
S=1000
K=0
while S<=1100:
    S=S+(S*(P*0.01))
    K=K+1
print ('Количество месяцев =', K)
print ('Размер вклада', S)    