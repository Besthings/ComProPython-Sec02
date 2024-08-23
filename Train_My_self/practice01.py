def find_single_occurrence_numbers(numbers: list) -> list:
    return [num for num in numbers if numbers.count(num) == 1]


print(find_single_occurrence_numbers([4, 5, 6, 4, 7, 5, 8]))
print(find_single_occurrence_numbers([1, 2, 2, 3, 3, 4, 4])) 
print(find_single_occurrence_numbers([1, 2, 3, 4, 5, 6])) 
print(find_single_occurrence_numbers([1, 1, 1, 1, 1])) 

    
# Anum = {}
#     str_num = [str(i) for i in numbers]
#     for key_num in str_num:
#         if key_num not in Anum:
#             Anum[key_num] = 1
#         else:
#             Anum[key_num] += 1

#     only_one_count = [nums for nums, count in Anum.items() if count == 1]
#     return(only_one_count)