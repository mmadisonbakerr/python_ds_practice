def list_manipulation(lst, command, location, value=None):
    if command == 'add':
        if location == 'beginning':
            lst.insert(0, value)
            return lst
        elif location == 'end':
            lst.append(value)
            return lst
        # elif location != 'beginning' or location != 'end':
        #     return None
    elif command == 'remove':
        if location == 'beginning':
            return lst.pop(0)
        elif location == 'end':
            return lst.pop()
        elif location != 'beginning' or location != 'end':
            return None
    # elif command != 'add' or command != 'remove':
    #     return None

    
        
    #     if command == 'add' and location == 'beginning':
    #         lst.insert(0, value)
    #         return lst
    # elif command == 'add' and location == 'end':
    #         lst.append(value)
    #         return lst
    # elif command == 'remove' and location == 'beginning':
    #         return lst.pop(0)
    # elif location == 'end' and location == 'end':
    #         return lst.pop()
    # elif location != 'beginning' or 'end':
    #         return None
    # elif command != 'add' or 'remove':
    #         return None
        
# Mutate lst to add/remove from beginning or end.

#     - lst: list of values
#     - command: command, either "remove" or "add"
#     - location: location to remove/add, either "beginning" or "end"
#     - value: when adding, value to add

#     remove: remove item at beginning or end, and return item removed

lst = [1, 2, 3]

print(list_manipulation(lst, 'remove', 'end'))
        # 3

print(list_manipulation(lst, 'remove', 'beginning'))
        # 1

print(lst)
#         # [2]

#     # add: add item at beginning/end, and return list

lst = [1, 2, 3]

print(list_manipulation(lst, 'add', 'beginning', 20))
#         # [20, 1, 2, 3]

print(list_manipulation(lst, 'add', 'end', 30))
#         # [20, 1, 2, 3, 30]

print(lst)
#         # [20, 1, 2, 3, 30]

#     # Invalid commands or locations should return None:

print(list_manipulation(lst, 'foo', 'end')) 
# is None
#         # True

print(list_manipulation(lst, 'add', 'dunno')) 
# is None
#         # True
