print ('Введите целое положительное число А')
A= int(input())
print ('Введите целое положительное число В, большее А')
B=int (input())
for i in range (A, B+1):
    for k in range (i):
        print (i)