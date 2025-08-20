#you are given 3 integer angles of triangle.tell whether the triangle is valid or not

a1 = int(input("Enter the first number: "))
a2 = int(input("Enter the second number: "))
a3 = int(input("Enter the third number: "))

if a1 > 0 and a2 > 0 and a3 > 0 and (a1 + a2 + a3 == 180):
  print("The triangle is valid.")
else:
  print("The triangle is not valid.")
  