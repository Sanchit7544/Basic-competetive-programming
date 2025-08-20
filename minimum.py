#write a program to input three numbers and print the minimum among them 

A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
C = int(input("Enter the third number: "))

if A > B and A > C :
   print("A is the minimum no.")
elif B < A and B < C :
   print("B is the minimum no.")

else:
  print("C is minimum.")
  