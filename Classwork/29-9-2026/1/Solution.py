num = input()
# digits = num.split()
# num1, num2 = int(digits[0]), int(digits[2])
# operator = digits[1]

num1, operator, num2 = num.split()
num1, num2 = int(num1), int(num2)

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