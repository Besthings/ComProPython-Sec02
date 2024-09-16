
try:
    y = int(input("Enter your numbers: "))
    x = 1 / y
    print("x = ", x)
except ZeroDivisionError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error: {e}")

print("End of program")