def group_anagrams(words: list) -> list:
    anagram_dict = {}
    for word in words:
        lower_word = word.lower()
        sorted_word = ''.join(sorted(lower_word))

        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]

    return list(anagram_dict.values())

# Example usage:
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

words2 = ["listen", "silent", "enlist", "hello", "world"]
print(group_anagrams(words2))
# Output: [["listen", "silent", "enlist"], ["hello"], ["world"]]
