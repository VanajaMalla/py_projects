# Descrption: 

# This Simple calculator project is based on python concepts : Variables and data types

print("*********** Simple Calculator ************")
print("Operations menu")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")

replay = 'Y'

while replay == 'Y':
    choice = int(input("Select your Choice of operation from menu :"))
    if choice == 1:
        a,b = map(int,input("Enter a,b: ").split(","))
        print(f"Sum of {a} and {b} is {a+b}")
    elif choice == 2:
        a,b = map(int,input("Enter a,b: ").split(","))
        print(f"Difference between {a} and {b} is {a-b}")
    elif choice == 3:
        a,b = map(int,input("Enter a,b: ").split(","))
        print(f"Product of {a} and {b} is {a*b}")
    elif choice == 4:
        a,b = map(int,input("Enter a,b: ").split(","))
        print(f"Division of {a} by {b} is {round(a/b,3)}")
    else:
        print("Invalid Choice")
    replay = input("Do you want to Countinue (Y/n):")
print("Thank You")
