def min_max_keys(d):
    return (min(d.keys()), max(d.keys()))

    
"""Return tuple (min-keys, max-keys) in d."""

print(min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'}))
        # (1, 10)

"""Works with any kind of key that can be compared, like strings:"""

print(min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"}))
        # ('apple', 'cherry')
    