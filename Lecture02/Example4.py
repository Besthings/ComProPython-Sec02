# คำนวนเปอร์เซ็นต์ผู้ชายและผู้หญิงในห้อง

male = int(input("ใส่จำนวนผู้ชาย: "))
female = int(input("ใส่จำนวนผู้หญิง: "))
total = male + female

male_percentage = (male / total) * 100
female_percentage = (female / total) * 100

# สูตรหาเปอร์เซ็นต์ คือ (ผู้ชาย x 100) / รวมทั้งหมด
#       หรือ        (ผู้หญิง / รวมทั้งหมด) x 100

print("เปอร์เซ็นต์ของผู้ชายคือ: ", format(male_percentage, ".2f" ), "%")
print("เปอร์เซ็นต์ของผู้หญิงคือ: ", format(female_percentage, ".2f" ), "%")