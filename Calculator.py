print("Calculator")
print("")

result = float(input("Please enter a number: "))

while True:
    operator = input(
        "Please enter an operator +, -, *, / (enter = if you wish to calculate): ")
    if operator == "=":
        break

    if operator not in ("+", "-", "*", "/"):
        print("Invalid operator. Try again")
        continue

    num = float(input("Please enter the next number: "))

    if operator == "+":
        result += num
    elif operator == "-":
        result -= num
    elif operator == "*":
        result *= num
    elif operator == "/":
        result /= num

print("Result:", result)
