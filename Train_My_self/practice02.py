def find_repeated_substrings(s: str) -> list:
    substring_count = {}
    result = []
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            substring = s[i:j] 
            # คือการเช็คค่า
            if substring in substring_count: 
                substring_count[substring] += 1
            else:
                substring_count[substring] = 1 
    for substring, count in substring_count.items():
        if count > 1:
            result.append(substring)
    return result   
    
print(find_repeated_substrings("banana"))
# Output: ['an', 'ana', 'na']

print(find_repeated_substrings("abcdefg"))
# Output: []

print(find_repeated_substrings("abcabcabc"))
# Output: ['ab', 'abc', 'abca', 'abcab', 'abcabc', 'bc', 'bca', 'bcab',
    # 'bcabc', 'ca', 'cab', 'cabc ']

print(find_repeated_substrings("aaaa"))
# Output: ['aa', 'aaa ']