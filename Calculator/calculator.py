def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def input_number(prompt):
    return float(input(prompt))
