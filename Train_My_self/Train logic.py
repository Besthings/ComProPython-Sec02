def sum_of_numbers(numbers: list) -> int:
    return sum(numbers)

numbers = [1, 2, 3, 4, 5]
print(sum_of_numbers(numbers))
# เอาต์พุตที่คาดหวัง: 15

numbers = [10, -2, 33, -5]
print(sum_of_numbers(numbers))
# เอาต์พุตที่คาดหวัง: 36

# ***************************************************************

def average(numbers: list) -> float:
    return sum(numbers) / len(numbers)

numbers = [10, 20, 30, 40, 50]
print(average(numbers))
# เอาต์พุตที่คาดหวัง: 30.0

numbers = [5, 10, 15]
print(average(numbers))
# เอาต์พุตที่คาดหวัง: 10.0

# ***************************************************************

def find_max(numbers: list) -> int:
    return max(numbers)

numbers = [1, 5, 3, 9, 2]
print(find_max(numbers))
# เอาต์พุตที่คาดหวัง: 9

numbers = [-5, -1, -10, -3]
print(find_max(numbers))
# เอาต์พุตที่คาดหวัง: -1

# ***************************************************************

def is_even(number: int) -> bool:
    return number % 2 == 0

number = 4
print(is_even(number))
# เอาต์พุตที่คาดหวัง: True

number = 7
print(is_even(number))
# เอาต์พุตที่คาดหวัง: False

# ***************************************************************

def count_characters(text: str) -> int:
    return len(text)

text = "hello"
print(count_characters(text))
# เอาต์พุตที่คาดหวัง: 5

text = "openai"
print(count_characters(text))
# เอาต์พุตที่คาดหวัง: 6

# ***************************************************************

def is_positive(number: int) -> bool:
    return number >= 0

number = 10
print(is_positive(number))
# เอาต์พุตที่คาดหวัง: True

number = -5
print(is_positive(number))
# เอาต์พุตที่คาดหวัง: False