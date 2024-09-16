try:
    y = int(input("Enter a number: "))
    result = 1 / y
    print(f"Result = {result}")
except Exception as e:
    print("Error:", e)
finally:
    print("Finally block")

print("End of program")