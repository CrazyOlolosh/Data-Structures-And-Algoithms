def first_non_repeating_char(s):
    for i in s:
        if s.count(i) == 1:
            return i
    return None


def first_non_repeating_char_2(string):
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char in string:
        if char_counts[char] == 1:
            return char
    return None


print(first_non_repeating_char('leetcode'))
print(first_non_repeating_char('hello'))
print(first_non_repeating_char('aabbcc'))


"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None
"""
