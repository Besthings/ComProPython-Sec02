with open('sales.txt', 'r') as sales_file:
    total = 0
    for line in sales_file:
        amount = float(line)
        print(format(amount, '.2f'))
        total += amount
    print(total)


