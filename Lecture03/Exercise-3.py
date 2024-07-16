hours_work = int(input("Enter the number of hours worked: "))
pay_rate = int(input("Enter the hourly pay rate: "))
standard_salary = 40*pay_rate

if hours_work <= 40:
    print("The gross pay is$", hours_work*pay_rate)
elif hours_work > 40:
    ot = hours_work - 40
    print("The gross pay is$", standard_salary+(ot*pay_rate*1.5))