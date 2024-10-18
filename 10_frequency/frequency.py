def frequency(lst, search_term):
    return lst.count(search_term)  
    
    """Return frequency of term in lst.
    
        >>> 
        3
        
        >>> 
        0
    """
    
print(frequency([1, 4, 3, 4, 4], 4))
# 3
print(frequency([1, 4, 3], 7))
# 0