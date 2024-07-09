name = input("what is your name? ")
age = int(input("How old are you? "))
income = float(input("What is your income? "))

print("Here is the data you entered: ")
print("Name:", name)
print("Age:", age)
print("Income:", format(income, "12,.2f"))