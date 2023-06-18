def remove_duplicates(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            del nums[i]
        else:
            i += 1
    return len(nums)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = remove_duplicates(nums)
print("New length:", new_length)
print("Unique values in list:", nums[:new_length])


"""
    EXPECTED OUTPUT:
    ----------------
    New length: 5
    Unique values in list: [0, 1, 2, 3, 4]
"""
