def two_oldest_ages(ages):
    ages = sorted(ages)
    if ages[-2] == ages[-1]:
        return ages[-3], ages[-1] 
    else:
        return ages[-2], ages[-1]
    
    #     uniq_ages = set(ages)
    # oldest = sorted(uniq_ages)[-2:]
    # return tuple(oldest)


    """Return two distinct oldest ages as tuple (second-oldest, oldest).. """

print(two_oldest_ages([1, 2, 10, 8]))      
        # (8, 10)

print(two_oldest_ages([6, 1, 9, 10, 4]))     
        # (9, 10)

"""Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:"""

print(two_oldest_ages([1, 5, 5, 2]))      
        # (2, 5)
   

    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.