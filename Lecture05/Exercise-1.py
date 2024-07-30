def is_armstrong(numbers):
    digits = str(numbers)
    num_digits = len(digits)
    total = 0
    for digit in digits:
        total += int(digit)**num_digits
    if total == numbers:
        return True
    else:
        return False

A = int(input("Enter nums: "))
print(is_armstrong(A))
