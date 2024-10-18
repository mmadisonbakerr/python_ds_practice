def last_element(lst):
    return None if lst == [] else lst[-1]

    # if lst:
    #     return lst[-1]
    
    """Return last item in list (None if list is empty.
    
        >>> 
        3
        
        >>>  is None
        True
    """
print(last_element([1, 2, 3]))
print(last_element([]))
