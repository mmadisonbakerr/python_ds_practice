def compact(lst):
    return [item for item in lst if item]

# Return a copy of lst with non-true elements removed.

print(compact([0, 1, 2, '', [], False, (), None, 'All done']))
        # [1, 2, 'All done']

# In Python, values like 0, False, "" (empty string), and None are considered "falsy."
# The list comprehension iterates over each item in my_list.
# If the item is truthy (i.e., not falsy), it is included in the filtered_list.