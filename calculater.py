x = float(input("enter first number: "))
op = input("enter the opretion: ")
y = float(input("enter second number: "))
if op == "+":
    z = x + y
elif op == "-":
    z =x - y
elif op == "*":
    z = x*y
elif op == "/":
    z = x/y
elif op == "**":
    z = x ** y
else:
    print("ronge oparetion")
print(f"{z:,}")