def sum_floats(nums):
    sum = 0
    for num in nums:
        if isinstance(num, float):
            sum += num
    return sum

    # return sum([num for num in nums if isinstance(num, float)])

    """Return sum of floating point numbers in nums."""
    
print(sum_floats([1.5, 2.4, 'awesome', [], 1]))
        # 3.9
        
print(sum_floats([1, 2, 3]))
        # 0

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!
