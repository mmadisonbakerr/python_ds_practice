def find_the_duplicate(nums):
    seen = set()
    dupes = []
    for x in nums:
        if x in seen:
            dupes.append(x)
        else:
            seen.add(x)
    return None if dupes == [] else dupes[0]

#   seen = set()

    # for num in nums:
    #     if num in seen:
    #         return num
    #     seen.add(num)

    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None """

print(find_the_duplicate([1, 2, 1, 4, 3, 12]))
        # 1

print(find_the_duplicate([6, 1, 9, 5, 3, 4, 9]))
        # 9

print(find_the_duplicate([2, 1, 3, 4]) )
# is None
        # True
   
