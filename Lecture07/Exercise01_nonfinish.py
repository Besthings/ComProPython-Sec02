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
# 5. หาผู้เข้าร่วมที่สามารถชอบภาษาได้เหมือนกันทั้งหมด

survey_results_sets = [set(Part) for Part in survey_results]

#* 1. ระบุภาษาที่ผู้เข้าร่วมทุกคนสามารถเขียนได้*
all_language_part = set.intersection(*survey_results_sets)
print("All participant can write it: ", all_language_part)

#* 2. หาภาษาที่ผู้เข้าร่วมสามารถใช้ภาษานี้ได้เพียงคนเดียว*
count_language = {}
for Parts in survey_results_sets:
    for languages in Parts:
        if languages in count_language:
            count_language[languages] += 1
        else:
            count_language[languages] = 1

languages_chosen_once = {language for language, count in count_language.items() if count == 1}
print("Languages chosen by only one participant: ", languages_chosen_once)

# 3. ให้นับจำนวนภาษาทั้งหมดที่ผู้เข้าร่วมเขียนเป็น
print("Number of unique languages: ", len(survey_results_sets))

# 4. ลิสต์ผู้เข้าร่วม 2 คน ที่เลือกภาษา java
languages_chosen_twice = {language for language, count in count_language.items() if count == 2}
print("Languages chosen by exactly two participants: ", languages_chosen_twice)

# 5. หาผู้เข้าร่วมที่สามารถชอบภาษาได้เหมือนกันทั้งหมด

matching_participants = {}
for i in range(len(survey_results_sets)):
    for j in range(i + 1, len(survey_results_sets)):
        
        if survey_results_sets[i] == survey_results_sets[j]:
            languages = tuple(survey_results_sets[i])
            if languages in matching_participants:
                matching_participants[languages].append(j + i)
            else:
                matching_participants[languages] = [i + 1, j + 1]

for languages, matching_participants in matching_participants.items():
    print("Participants with the same set of languages", matching_participants)