num = input()
digi_list = list(num)
digi = []
digits = []

for i in range(len(digi_list)):
    if digi_list[i] != " ":
        digi.append(digi_list[i])
    if digi_list[i] == " " or i == len(digi_list) - 1:
        digits.append("".join(digi))
        digi = []
    

num1, num2 = int(digits[0]), int(digits[2])
operator = digits[1]

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


