num = input()

num1 = ""
num2 = ""
operator = ""

for ch in num:
    if ch.isdigit():
        if operator == "":
            num1 += ch
        else:
            num2 += ch
    elif ch != " ":
        operator = ch

num1 = int(num1)
num2 = int(num2)

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