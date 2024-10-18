def multiply_even_numbers(nums):
    sum = 1
    for num in nums:
        if num % 2 == 0:
            sum *= num
    return sum

    """Multiply the even numbers.
    
        >>> 
        48
    
        >>> 
        4
    
    If there are no even numbers, return 1.
    
        >>> 
        1
    """

print(multiply_even_numbers([2, 3, 4, 5, 6]))
print(multiply_even_numbers([3, 4, 5]))
print(multiply_even_numbers([1, 3, 5]))