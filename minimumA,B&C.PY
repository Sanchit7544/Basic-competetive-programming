A = int(input("enter a number (A):"))
B = int(input("enter a number (B):"))
C = int(input("enter a number (c):"))

if A<B:
    print("number is minimum",A)
elif B<C: 
    print("number is minimum",B)
elif C<A: 
    print("number is minimum",C)
else:
    print("all the numbers are equal")