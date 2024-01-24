def letters_in_either(word1, word2):
    return sorted(list(set(word1) | set(word2)))

def letters_in_both(word1, word2):
    return sorted(list(set(word1) & set(word2)))

def letters_in_either_not_both(word1, word2):
    return sorted(list(set(word1) ^ set(word2)))


result1 = letters_in_either("hello", "world")
result2 = letters_in_both("hello", "world")
result3 = letters_in_either_not_both("hello", "world")
print(result1, result2, result3)
