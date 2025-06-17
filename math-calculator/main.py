def math_calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    elif operator == '%':
        return num1 % num2
    elif operator == '**':
        return num1 ** num2
    else:
        raise ValueError("Unsupported operator.")

# Input from user
try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /, %, **): ")
    num2 = float(input("Enter second number: "))

    result = math_calculator(num1, operator, num2)
    print(f"Result: {num1} {operator} {num2} = {result}")

except Exception as e:
    print(f"Error: {e}")
