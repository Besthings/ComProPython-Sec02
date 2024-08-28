months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

dayInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

daysOfweek = [
    ["mon"], ["tue"], ["wed"], ["thurs"], ["fri"], ["sat"], ["sun"]
]

# รับข้อมูลเดือนจากผู้ใช้
selected_month = input("Enter the name of the month: ").capitalize()

if selected_month in months:
    # หาตำแหน่งของเดือนในลิสต์
    month_index = months.index(selected_month)
    
    print(f"\nMonth: {selected_month}")
    print(f"Days in {selected_month}: {dayInMonth[month_index]}")
    
    # สมมุติว่าเดือนเริ่มต้นที่วันจันทร์
    start_day_index = daysOfweek.index(["mon"])  # สามารถเปลี่ยนเป็นค่าที่ผู้ใช้เลือกหรือคำนวณจากปีและเดือน
    
    print("Start day:", daysOfweek[start_day_index][0])
    
    # แสดงวันที่ในรูปแบบปฏิทิน
    print("\nSu Mo Tu We Th Fr Sa")
    
    # จำนวนวันในสัปดาห์ที่เริ่มต้นของเดือนนี้
    print(" " * (start_day_index * 3), end="")
    
    for day in range(1, dayInMonth[month_index] + 1):
        print(f"{day:2d} ", end="")
        if (day + start_day_index) % 7 == 0:
            print()
    
    print("\n")
else:
    print("Invalid month name. Please enter a valid month.")