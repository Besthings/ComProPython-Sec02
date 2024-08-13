# ตารางเช็คชื่อ 5 วัน
attendance_week = [
    ["Alice", "Bob", "Charlie", "David"],   # day1
    ["Alice", "Charlie", "David"],          # day2
    ["Alice", "Bob", "David"],              # day3
    ["Alice", "David", "Eve"],              # day4
    ["Bob", "Charlie", "David"]             # day5
]

# 1.หานักเรียนที่มาเรียนครบทุกวัน
# 2.กำหนดนักเรียนที่ขาดอย่างน้อย 1 วัน
# 3.สร้างลิสต์นักเรียนที่มาเรียนในวันแรก แต่ขาดวันสุดท้าย
# 4.คำนวณจำนวนนักเรียนที่ไม่ซ้ำกันทั้งหมดที่เข้าเรียนอย่างน้อย 1 วัน

# เปลี่ยนจาก list ไปเป็น set
attendance_sets = [set(day) for day in attendance_week]
print(attendance_sets)

#* 1.หานักเรียนที่มาเรียนครบทุกวัน*
present_every_day = set.intersection(*attendance_sets)
print("Present every day: ", present_every_day)

#* 2.กำหนดนักเรียนที่ขาดอย่างน้อย 1 วัน*
all_student = set.union(*attendance_sets)
absent_at_least_oneday = all_student - present_every_day
print("Absent at least one day: ", absent_at_least_oneday)

#* 3.สร้างลิสต์นักเรียนที่มาเรียนในวันแรก แต่ขาดวันสุดท้าย*
first_day_present = attendance_sets[0]
last_day_absent = attendance_sets[-1]
first_day_but_not_last = list(first_day_present - last_day_absent)
print("Present on first day but absent on last day: ", first_day_but_not_last)

#* 4.คำนวณจำนวนนักเรียนที่ไม่ซ้ำกันทั้งหมดที่เข้าเรียนอย่างน้อย 1 วัน*
unique_students_count = len(all_student)
print("Total unique students: ", unique_students_count)