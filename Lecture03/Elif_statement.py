num_employees = int(input("Enter the number of employees: "))

if num_employees < 50:
    print("Small company")
elif num_employees < 250:
    print("Medium company")
elif num_employees > 250:
    print("Large company")