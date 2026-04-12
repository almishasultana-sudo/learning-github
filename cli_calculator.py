import sys

# check if enough arguments are given
if len(sys.argv) < 4:
    print("Usage: python cli_calculator.py <operation> <num1> <num2>")
    sys.exit()

operation = sys.argv[1]

try:
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])
except ValueError:
    print("Please enter valid numbers.")
    sys.exit()

if operation == "add":
    result = num1 + num2

elif operation == "sub":
    result = num1 - num2

elif operation == "mul":
    result = num1 * num2

elif operation == "div":
    if num2 == 0:
        print("Cannot divide by zero.")
        sys.exit()
    result = num1 / num2

else:
    print("Unknown operation.")
    sys.exit()

print("Result =", result)
print("Thank you for using CLI Calculator!")