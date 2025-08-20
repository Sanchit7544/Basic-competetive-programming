a = int(input("Enter an Angle : "))
b = int(input("Enter an Angle : "))
c = int(input("Enter an Angle : "))
if a>90 or b>90 or c>90 :
    print("The triangle is obtuse triangle")
elif a == 90 or b==90 or c==90:
    print("The triangle is right angle triangle")
else:
    print("The triangle is a acute triangle")