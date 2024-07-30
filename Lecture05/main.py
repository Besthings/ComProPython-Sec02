import math_operations

A = float(input("Enter first nums: "))
B = float(input("Enter second nums: "))

resultAdd = math_operations.add(A,B)
resultSubtract = math_operations.subtract(A,B)
resultMultiply = math_operations.multiply(A,B)
resultDivide = math_operations.divide(A,B)

print(f"Sum is {resultAdd}")
print(f"Subtract is {resultSubtract}")
print(f"Multiply is {resultMultiply}")
print(f"Divide is {resultDivide}")
