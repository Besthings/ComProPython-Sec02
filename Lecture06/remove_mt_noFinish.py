fruits_width_duplicates = ["apple", "banana", "apple", "cherry", "apple", "kiwi"]
remove_list = []
for fruit in fruits_width_duplicates:
    if fruit == "apple":
        fruits_width_duplicates.pop()

print(f"Fruits after remove: {fruits_width_duplicates}")
print(remove_list)