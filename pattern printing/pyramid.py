n = int(input("enter the no. of stars:"))
for i in range(n):
    for j in range(i,n-1):
        print("*", end='')
    print()