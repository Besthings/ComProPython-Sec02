score = float(input("Enter a test score: "))

while score < 0 or score > 100:
    print("Error: The score can't be negative")
    print("or greater than 100. ")
    score = float(input("Enter the correct score: "))