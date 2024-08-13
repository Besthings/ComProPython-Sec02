# Survey results (each list represents a participant's choices) | แบบสำรวจจากผู้เข้าร่วม
survey_results = [
    ["Python", "JavaScript", "C++"],  # Participant 1
    ["Python", "JavaScript", "C#"],   # Participant 2
    ["Python", "Java"],               # Participant 3
    ["Python", "C++", "JavaScript"],  # Participant 4
    ["Python", "JavaScript", "C++", "Java"],  # Participant 5
]

# 1. ระบุภาษาที่ผู้เข้าร่วมทุกคนสามารถเขียนได้
# 2. หาภาษาที่ผู้เข้าร่วมสามารถใช้ภาษานี้ได้เพียงคนเดียว
# 3. ให้นับจำนวนภาษาทั้งหมดที่ผู้เข้าร่วมเขียนเป็น
# 4. ลิสต์ผู้เข้าร่วม 2 คน ที่เลือกภาษา java
# 5. หาผู้เข้าร่วมที่สามารถเขียนภาษาได้เหมือนกันทั้งหมด

survey_results_sets = [set(Part) for Part in survey_results]

#* 1. ระบุภาษาที่ผู้เข้าร่วมทุกคนสามารถเขียนได้*
all_language_part = set.intersection(*survey_results_sets)
print("All participant can write it: ", all_language_part)

#* 2. หาภาษาที่ผู้เข้าร่วมสามารถใช้ภาษานี้ได้เพียงคนเดียว*
all_participants = set.union(*survey_results_sets)
one_part = all_participants | all_language_part
print(one_part)