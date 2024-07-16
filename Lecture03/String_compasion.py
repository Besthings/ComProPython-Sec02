# Program to compare strings "Mary" and "Mark"

# Define the strings
string1 = "Mary"
string2 = "Mark"

# Compare the strings for equality
if string1 == string2:
    print(f"'{string1}' and '{string2}' are equal")
else:
    print(f"'{string1}' and '{string2}' aren't equal")

# Lexicographical comparison
if string1 < string2:
    print(f"'{string1}' comes before '{string2}' in lexicographical order.")
elif string1 > string2:
    print(f"'{string1}' comes after '{string2}' in lexicographical order.")

# Case-insensitive comparison
if string1.lower() == string2.lower():
    print(f"'{string1}' and '{string2}' are eual when case is ignored.")
else:
    print(f"'{string1}' and '{string2}' aren't eual when case is ignored.")