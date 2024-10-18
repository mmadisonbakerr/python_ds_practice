def includes(collection, sought, start=None):
    if isinstance(collection, list):
        collection = collection[start:]
        return (True if sought in collection else False)
    elif isinstance(collection, dict):
        return (True if sought in collection.values() else False)
    return (True if sought in collection else False)

#     if isinstance(collection, dict):
#         return sought in collection.values()

#     if start is None or isinstance(collection, set):
#         return sought in collection

#     return sought in collection[start:]

#     elif sought in collection:
#         return True
#     else:
#         return False
        
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered."""

print(includes([1, 2, 3], 1))
        # True

print(includes([1, 2, 3], 1, 2))
        # False

print(includes("hello", "o"))
        # True

print(includes(('Elmo', 5, 'red'), 'red', 1))
        # True

print(includes({1, 2, 3}, 1))
        # True

print(includes({1, 2, 3}, 1, 3) )
        #"start" ignored for sets!)
        # True

print(includes({"apple": "red", "berry": "blue"}, "blue"))
        # True
    