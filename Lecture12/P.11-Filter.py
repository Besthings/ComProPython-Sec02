numbers = [1, 2, 3, 4, 5]
even_number = list(filter(lambda x: x % 2 == 0, numbers))
odd_number = list(filter(lambda x: x % 2 != 0, numbers))
print(even_number)
print(odd_number)