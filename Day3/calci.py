print("======CALCULATOR======")
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
print("\nSelect Operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
print("6.Exponential")
print("7.Floor Division")
choice = int(input("Enter choice(1-7): "))
if choice==1:
    print("Addition: ", num1 + num2)
elif choice==2:
    print("Subtraction: ", num1 - num2)
elif choice==3:
    print("Multiplication: ", num1 * num2)
elif choice==4:
    print("Division: ", num1 / num2)
elif choice==5:
    print("Modulus: ", num1 % num2)
elif choice==6:
    print("Exponenetial: ", num1 ** num2)
elif choice==7:
    print("Floor Division: ", num1 // num2)
else:
    print("Invalid Choice")