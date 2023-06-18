def find_max_min(numbers):
    if len(numbers) == 0:
        return (None, None)
    elif len(numbers) == 1:
        return (numbers[0], numbers[0])
    else:
        max_number = numbers[0]
        min_number = numbers[0]
        for number in numbers:
            if number > max_number:
                max_number = number
            elif number < min_number:
                min_number = number
        return (max_number, min_number)


def find_max_min_2(numbers):
    if len(numbers) == 0:
        return (None, None)
    elif len(numbers) == 1:
        return (numbers[0], numbers[0])
    else:
        max_number = max(numbers)
        min_number = min(numbers)
        return (max_number, min_number)


print(find_max_min([5, 3, 8, 1, 6, 9]))
print(find_max_min_2([5, 3, 8, 1, 6, 9]))

"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
"""
