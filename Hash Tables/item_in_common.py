def item_in_common_naive(list1, list2):
    '''Complexity: O(n^2)
    Space complexity: O(1)
    '''
    for item in list1:
        if item in list2:
            return True
    return False


def item_in_common_set_intersection(list1, list2):
    '''Complexity: O(n)
    Space complexity: O(n)
    '''
    return len(set(list1).intersection(set(list2))) > 0


def item_in_common(list1, list2):
    '''Complexity: O(n)
    Space complexity: O(n)
    '''
    my_dict = {}
    for item in list1:
        my_dict[item] = True
    for item in list2:
        if item in my_dict:
            return True
    return False


list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(item_in_common(list1, list2))
print(item_in_common_naive(list1, list2))
print(item_in_common_set_intersection(list1, list2))
