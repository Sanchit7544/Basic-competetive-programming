A = int(input("Enter a number: "))

rev = 0
temp = A
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if rev == A:
    print("Yes it is a palindrome")
else:
    print("No it is not a palindrome")
