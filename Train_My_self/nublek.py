# จงทำตามนี้หาผลลัพธ์ที่ตัวเลขในลิสต์รวมกันแล้วได้ 6 print((sum_of_with_nums([1,3,5,7], 6))) -> [1, 5]

def sum_of_with_nums(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
               return [nums[i], nums[j]]
    return []
                

        
print((sum_of_with_nums([1,9,5,7], 10)))