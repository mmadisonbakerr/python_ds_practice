def remove_every_other(lst):
    return lst[0::2]

"""Return a new list of other item."""

lst = [1, 2, 3, 4, 5]

print(remove_every_other(lst))
        # [1, 3, 5]

"""This should return a list, not mutate the original:"""

print(lst)
        # [1, 2, 3, 4, 5]
