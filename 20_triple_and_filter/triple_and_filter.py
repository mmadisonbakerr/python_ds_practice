def triple_and_filter(nums):
    return [num * 3 for num in nums if num % 4 == 0]

    # for num in nums: 
    #     if num % 4 == 0:
    #         num = num * 3
    #         result.append(num)
    # print(result)

# return the result into an array 
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.
    
        >>> 
        [12]
        
        >>> 
        [24, 36]
        
        >>> 
        []
    """
print(triple_and_filter([1, 2, 3, 4]))
print(triple_and_filter([6, 8, 10, 12]))
print(triple_and_filter([1, 2]))