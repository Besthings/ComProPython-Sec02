print("Please select operation -")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

select = int(input("Enter number form 1,2,3,4: " ))

if select not in [1, 2, 3, 4]:
    print("invalid input")
else:

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if  select == 1:
        print(f"{num1} + {num2} =", num1+num2)

    elif select == 2:
        print(f"{num1} - {num2} =", num1-num2)

    elif select == 3:
        print(f"{num1} x {num2} =", num1*num2)

    elif select == 4:
        if num2 == 0:
            print("Cant Divide with 0")
        else:
            print(f"{num1} / {num2} =", num1/num2)