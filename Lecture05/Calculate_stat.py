def calculate_stats(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total_sum, average, maximum, minimum

numbers = [5, 10, 15, 20, 25]
total, avg, max_num, min_num = calculate_stats(numbers)

print(f"Total Sum: {total}")
print(f"Total Average: {avg}")
print(f"Total Maximum: {max_num}")
print(f"Total Minimum: {min_num}")

# numbers = []
# max = 5

# for i in range(max):
#     numbers = int(input(f"Enter {i+1} number: "))