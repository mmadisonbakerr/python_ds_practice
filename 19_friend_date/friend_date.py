def friend_date(a, b):
    for x in a[2]:
        if x in b[2]:
            return True
    else: 
        return False
    
    #   if set(a[2]) & set(b[2]):
    #     return True
    # else:
    #     return False
    
    # return [True if x in b[2] else False for x in a[2] if x in b]

    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> 

        >>> )
        False

        >>> 
        True
    """
elmo = ('Elmo', 5, ['hugging', 'being nice'])
sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

print(friend_date(elmo, sauron))
print(friend_date(sauron, gandalf))