print("=== Python Calculator ===")

first = float(input("First number: "))
operator = input("Operator (+, -, *, /): ")
second = float(input("Second number: "))

if operator == "+":
    result = first + second

elif operator == "-":
    result = first - second

elif operator == "*":
    result = first * second

elif operator == "/":
    if second == 0:
        result = "Cannot divide by zero"
    else:
        result = first / second

else:
    result = "Invalid operator"

print("Result:", result)