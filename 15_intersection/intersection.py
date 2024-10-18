def intersection(l1, l2):
    return [x for x in l1 if x in l2]

    # result = []
    # for x in l1:
    #     if x in l2:
    #         result.append(x)
    # return result 

    """Return intersection of two lists as a new list::"""


print(intersection([1, 2, 3], [2, 3, 4]))
        # [2, 3]
        
print(intersection([1, 2, 3], [1, 2, 3, 4]))
    # [1, 2, 3]
        
print(intersection([1, 2, 3], [3, 4]))
    # [3]
        
print(intersection([1, 2, 3], [4, 5, 6]))
    # []
