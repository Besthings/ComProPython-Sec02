# sales = float(input("Enter the amount of sales: "))
# comm_rate = float(input("Enter the commission rate: "))
# commission = sales * comm_rate
# print("The commission is $", format(commission, ".2f"))

# sales = float(input("Enter the amount of sales: "))
# comm_rate = float(input("Enter the commission rate: "))
# commission = sales * comm_rate
# print("The commission is $", format(commission, ".2f"))

# sales = float(input("Enter the amount of sales: "))
# comm_rate = float(input("Enter the commission rate: "))
# commission = sales * comm_rate
# print("The commission is $", format(commission, ".2f"))

keep_going = 'y'

while keep_going == 'y':
    sales = float(input("Enter the amount of sales: "))
    comm_rate = float(input("Enter the commission rate: "))

    commmision = sales * comm_rate

    print(f"The commission is ${commmision:.2f}")

    keep_going = input("Do you want to calculate another", "commmision (Enter y for yes): ")