def mode(nums):
    most_common_num = nums[0]
    for num in nums:
        if nums.count(num) > nums.count(most_common_num):
            most_common_num = num
    return most_common_num
    
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times. """

print(mode([1, 2, 1]))
        # 1

print(mode([2, 2, 3, 3, 2]))
        # 2
   
