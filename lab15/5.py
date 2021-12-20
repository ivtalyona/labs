def Fact2 (N: int):
    s=1
    if N%2!=0:
        for i in range (1,N+1, 2):
            s=float (s*i)
            
    else:
        for k in range (2, N+1, 2):
            s=float (s*k)
            
    return s
print (' N')
N=int (input())
s=Fact2(N)
print (s)