def validate_wordPattern(pattern, s):
    map = {}
    s = s.split()
    for char, word in zip(pattern, s):
        if char not in map:
            map[char] = word
        else:
            if map[char] != word:
                return False
    return True


print(validate_wordPattern("abba", "dog cat cat dog"))
print(validate_wordPattern("gggg", "dog cat cat dog"))
