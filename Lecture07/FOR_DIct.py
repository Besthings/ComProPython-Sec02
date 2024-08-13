phonebook = {"Anirach": "777-1111", "Mickey": "777-2222", "Donald": "777-3333"}

phonebook["Bart"] = [1, 3, 5]

element = len(phonebook)
print("There are", element, "name in phonebook")

for key, value in phonebook.items():
    print(f"{key} phone number is: {value}")

phonebook["Bart"][1] = 9
print(phonebook)