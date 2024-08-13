student = {"name": "Alice", "age": 25, "grade": "A"}

# แก้ไขหรือเพิ่ม key และ value เข้าไปในตัว Dict ของ student
student["age"] = 26
student["major"] = "Computer Science"
print(student)

#ลบ key-value ทั้งคู่ออกจาก dict โดยใช้ 'del'
del student["grade"]
print(student)

#ลบ key-value ทั้งคูดโดยใช้ pop
remover_major = student.pop("major")
print(remover_major)
print(student)