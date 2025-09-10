n = int(input("Rows: "))

for i in range(n, 0, -1):
    print("*" * i, end="")

    print(" " * (2*(n-i)), end="")

    print("*" * i)