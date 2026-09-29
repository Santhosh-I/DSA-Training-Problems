num = input()

for i in range(len(num)):
    if num[i] in "+-*/":
        operator = num[i]
        num1 = int(num[:i])
        num2 = int(num[i+1:])

        break

if operator == "+":
    print("Sum =",num1 + num2)
elif operator == "-":
    print("Difference =",num1 - num2)
elif operator == "*":
    print("Product =",num1 * num2)
elif operator == "/":
    print("Quotient =",num1 // num2, "Remainder =",num1 % num2)
else:
    print("Invalid")