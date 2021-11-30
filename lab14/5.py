print ('Введите целое положительное число А')
A= int(input())
print ('Введите целое положительное число В')
B= int (input())
while A!=B:
    if A>B:
        A=A-B
    else:
        B=B-A
print ('НОД чисел А и В =',A)