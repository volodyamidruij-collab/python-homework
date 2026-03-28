a = 10
b = 2
operation = "+"

if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    if b == 0:
        print("Ділення на нуль")
    else:
        print(a / b)
else:
    print("Невідома операція")
