# main.py

from Calculator.calculator import input_number, add, sub, mul, div

if __name__ == "__main__":
    x = input_number("Enter the first number: ")
    y = input_number("Enter the second number: ")

    print("The sum of the two numbers is:", add(x, y))
    print("The difference of the two numbers is:", sub(x, y))
    print("The product of the two numbers is:", mul(x, y))
    print("The division of the two numbers is:", div(x, y))

    print("Whole code executed successfully")
