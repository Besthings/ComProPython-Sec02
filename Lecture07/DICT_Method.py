# Creating a dictionary
student = {'name': 'Alice', 'age': 26, 'major': 'Computer Science'}

# Dictionary methods
print(student.keys())   # Output: dict_keys(['name', 'age', 'major'])
print(student.values()) # Output: dict_values(['Alice', 26, 'Computer Science'])
print(student.items())  # Output: dict_items([('name', 'Alice'), ('age', 26), ('major', 'Computer Science')])

# Using get() method
print(student.get("name"))                # Output: Alice
print(student.get("grade", "Not Found"))  # Output: Not Found

# Using pop() method
major = student.pop("major")
print(major)                              # Output: Computer Science
print(student)                            # Output: {'name': 'Alice', 'age': 26}

# Using popitem() method
last_item = student.popitem()
print(last_item)                          # Output: ('age', 26)
print(student)                            # Output: {'name': 'Alice'}

# Using clear() method
student.clear()
print(student)                            # Output: {}
