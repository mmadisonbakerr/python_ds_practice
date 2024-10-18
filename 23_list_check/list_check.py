def list_check(lst):
    is_list = False
    for item in lst:
        if isinstance(item, list):
            is_list = True
        else:
            is_list = False
    return is_list
     
    #     for item in lst:
    #     if not isinstance(item, list):
    #         return False

    # return True
    
    """Are all items in lst a list?"""

print(list_check([[1], [2, 3]]))
        # True

print(list_check([[1], "nope"]))
        # False
