def find_sum_with_list(numbers:list, target:int) -> list:
    # สร้าง dictionary เพื่อเก็บตัวเลขที่เราได้พบไปแล้ว
    seen = {}
    # วนซ้ำไปยังตัวเลขทุกตัวใน list
    for num in numbers:
        # คำนวณหาตัวเลขที่ต้องการเพื่อให้ได้ผลบวกเป็น target
        complement = target - num
        # ตรวจสอบว่าตัวเลขที่ต้องการอยู่ใน dictionary หรือไม่
        if complement in seen:
            # ถ้าเจอแล้ว return ผลลัพธ์เป็น list ของตัวเลขสองตัว
            return [complement, num]
        # เก็บตัวเลขปัจจุบันไว้ใน dictionary
        seen[num] = True
    # ถ้าไม่มีคู่ที่ตรงกับเป้าหมายให้ return None
    return "No missing nums"

# ทดลองใช้งานฟังก์ชัน
print(find_sum_with_list([1, 2, 3, 4, 6], 6))  # output = [2, 4]
print(find_sum_with_list([1, 2, 5, 6, 7], 12))
print(find_sum_with_list([1, 2, 2, 7, 5], 4))
print(find_sum_with_list([4, 2, 1, 4, 0], 12))
print(find_sum_with_list([6, 2, 5, 4, 1], 5))