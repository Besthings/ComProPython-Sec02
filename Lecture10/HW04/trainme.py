def get_pattern(word):
    # ฟังก์ชันนี้สร้าง "pattern" จากคำ โดยเปรียบเทียบตัวอักษรแต่ละตัว
    pattern = []
    for i in range(1, len(word)):
        if word[i] > word[i - 1]:
            pattern.append(1)   # ตัวอักษรตัวถัดไปมากกว่า -> เพิ่มขึ้น
        elif word[i] < word[i - 1]:
            pattern.append(-1)  # ตัวอักษรตัวถัดไปน้อยกว่า -> ลดลง
        else:
            pattern.append(0)   # ตัวอักษรเท่ากัน -> คงที่
    return tuple(pattern)  # แปลงเป็น tuple เพื่อใช้เป็น key ในดิกชันนารี

def group_by_pattern(words: list) -> list:
    pattern_dict = {}
    
    for word in words:
        pattern = get_pattern(word)  # สร้าง pattern ของคำแต่ละคำ
        
        if pattern in pattern_dict:
            pattern_dict[pattern].append(word)  # ถ้ามี pattern เดิมในดิกชันนารีแล้ว ให้เพิ่มคำเข้าไป
        else:
            pattern_dict[pattern] = [word]  # ถ้ายังไม่มี ให้สร้างลิสต์ใหม่สำหรับ pattern นี้
    
    return list(pattern_dict.values())  # ส่งคืนลิสต์ของกลุ่มคำ



# ตัวอย่างที่ 1
words = ["abc", "bcd", "ace", "xyz", "bda", "edf"]
print(group_by_pattern(words))
# เอาต์พุต: [["abc", "bcd", "xyz"], ["ace", "bda", "edf"]]

# ตัวอย่างที่ 2
words = ["aa", "bb", "cc", "abc", "cba"]
print(group_by_pattern(words))
# เอาต์พุต: [["aa", "bb", "cc"], ["abc", "cba"]]
