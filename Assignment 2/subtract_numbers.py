"""
Asks the user for two numbers and prints the result
of the first number minus the second number.
"""

def main():
    print("This program subtracts one number from another.")
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    sub=num1-num2
    print("The result is",float(sub))

if __name__ == '__main__':
    main()
