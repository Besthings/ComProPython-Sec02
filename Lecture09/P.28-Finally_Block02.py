try:
    # Ask user to input two numbers
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))

    # Perform the division
    result = numerator / denominator

except ZeroDivisionError:
    print("Error: Division by zero error")

except ValueError:
    print("Error: Invalid input. Please enter numeric values.")

finally:
    # This block will always run, regardless of errors
    print("Execution completed, whether an exception occurred or not.")

print("End of program")
