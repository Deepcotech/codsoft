def add(x, y):              #function for the addition 
    return x + y

def subtract(x, y):         #function for the subtraction
    return x - y

def multiply(x, y):         #function for the multiplication    
    return x * y

def divide(x, y):           #function for the division
    if y != 0:
        return x / y
    else:
        return "Error: Any number cannot be divided by zero"

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Enter operation (1/2/3/4): ")

if operation in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif operation == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif operation == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif operation == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input. Please enter a valid operation (1/2/3/4).")
