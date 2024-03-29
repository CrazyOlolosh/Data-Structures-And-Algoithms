def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = []
    hash_map = {}
    for i in range(len(nums)):
        if nums[i] in hash_map:
            result.append(hash_map[nums[i]])
            result.append(i)
            return result
        else:
            hash_map[target - nums[i]] = i
    return result


def two_sum_2(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
print(two_sum([1, 2, 3, 4, 5], 10))
print(two_sum([1, 2, 3, 4, 5], 7))
print(two_sum([1, 2, 3, 4, 5], 3))
print(two_sum([], 0))


"""
    EXPECTED OUTPUT:
    ----------------
    [0, 1]
    [1, 2]
    [0, 1]
    []
    [2, 3]
    [0, 1]
    []

"""
