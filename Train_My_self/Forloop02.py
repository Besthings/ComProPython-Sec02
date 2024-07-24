def count_char_types(input_string):
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0

    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1

    return uppercase_count, lowercase_count, digit_count

# ตัวอย่างการใช้งาน
input_string = input("Enter string: ")
upper, lower, digits = count_char_types(input_string)

print(f"จำนวนตัวอักษรพิมพ์ใหญ่: {upper}")
print(f"จำนวนตัวอักษรพิมพ์เล็ก: {lower}")
print(f"จำนวนตัวเลข: {digits}")