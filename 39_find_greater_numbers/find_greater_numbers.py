def find_greater_numbers(nums):
    count = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                count += 1

    return count
#     result = 0
#     big_num = nums[0]
#     for num in nums:
#         if nums == []:
#             return result
#         elif num > big_num:
#             result += 1
#     return result
    
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:  """

print(find_greater_numbers([1, 2, 3]))
        # 3

print(find_greater_numbers([6, 1, 2, 7]))
        # 4

print(find_greater_numbers([5, 4, 3, 2, 1]))
        # 0

print(find_greater_numbers([]))
        # 0
  