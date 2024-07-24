# ให้เขียนโปรแกรม Python ที่รับข้อมูลเป็นลิสต์ของตัวเลข และใช้ for loop 
# เพื่อหาตัวเลขที่มากกว่าค่าเฉลี่ยของตัวเลขในลิสต์นั้น 
# โดยไม่ใช้ฟังก์ชัน max() หรือ min() ในการหาค่าสูงสุดหรือต่ำสุดของลิสต์
# ตัวอย่าง:
# ถ้าเรียกใช้โปรแกรมกับลิสต์ [10, 5, 8, 12, 3, 7] 
# โปรแกรมควรพิมพ์เฉพาะตัวเลขที่มากกว่าค่าเฉลี่ยของลิสต์นี้คือ 10, 12.

list_numbers = [10, 5, 8, 12, 3, 7]
sum = 0

for i in list_numbers:
    sum += i

average = sum / len(list_numbers)
print("average is :", format(average, ".2f"))

for num in list_numbers:
    if num > average:
        print(num)
