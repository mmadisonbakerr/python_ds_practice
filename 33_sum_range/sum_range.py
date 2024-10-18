def sum_range(nums, start=0, end=None):
    sum = 0
    nums = nums[start:end]
    for num in nums:
        sum += num
    return sum

    # if end is None:
    #     end = len(nums)

    # return sum(nums[start:end + 1])


"""Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> 

        >>> 
        10

        >>> 
        9

        >>> 
        6

        >>> 
        9

    If end is after end of list, just go to end of list:

        >>> 
        9
    """
nums = [1, 2, 3, 4]
print(sum_range(nums))
print(sum_range(nums, 1))
print(sum_range(nums, end=2))
print(sum_range(nums, 1, 3))
print(sum_range(nums, 1, 99))