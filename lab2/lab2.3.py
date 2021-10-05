A=int(input())
B=int(input())
C=int(input())
if (C<A and C>B) or (C>A and C<B):
    p=(abs(A-C)*abs(B-C))
    print(p)
else:
    print("значение произведения вычислить нельзя")
