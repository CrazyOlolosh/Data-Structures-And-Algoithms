def find_longest_string(string_list):
    longest = ""
    for string in string_list:
        if len(string) > len(longest):
            longest = string
    return longest


string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)


"""
    EXPECTED OUTPUT:
    ----------------
    banana
"""
