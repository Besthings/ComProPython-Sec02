performance_data = {
    "Sales": {
        "Alice": [80, 85, 88, 90],
        "Bob": [70, 75, 78, 80],
        "Charlie": [60, 65, 70, 72],
    },
    "Engineering": {
        "David": [90, 92, 94, 95],
        "Eve": [85, 88, 87, 90],
        "Frank": [88, 87, 86, 85],
    },
    "HR": {
        "Grace": [70, 72, 74, 76],
        "Heidi": [65, 68, 70, 73],
        "Ivan": [60, 62, 64, 66],
    }
}

# 1. Calculate the average performance score for each employee.
# 2. Identify the top performer in each department based on their average score.
# 3. Determine the department with the highest average performance score.
# 4. Find employees who have shown continuous improvement.
# 5. Generate a summary report.

# 1. **คำนวณคะแนนเฉลี่ยด้านประสิทธิภาพสำหรับพนักงานแต่ละคน**
# 2. **ระบุผู้ที่ทำผลงานได้ดีที่สุดในแต่ละแผนกโดยพิจารณาจากคะแนนเฉลี่ย**
# 3. **กำหนดแผนกที่มีคะแนนประสิทธิภาพเฉลี่ยสูงสุด**
# 4. **ค้นหาพนักงานที่มีการปรับปรุงอย่างต่อเนื่อง**
# 5. **สร้างรายงานสรุป**

# **************************************************************************************

# 1. **คำนวณคะแนนเฉลี่ยด้านประสิทธิภาพสำหรับพนักงานแต่ละคน**
average_scores = {}
for department, employees in performance_data.items():
    average_scores[department] = {}
    for employee, scores in employees.items():
        average = sum(scores) / len(scores)
        average_scores[department][employee] = average
print(average_scores)

# 2. **ระบุผู้ที่ทำผลงานได้ดีที่สุดในแต่ละแผนกโดยพิจารณาจากคะแนนเฉลี่ย**
