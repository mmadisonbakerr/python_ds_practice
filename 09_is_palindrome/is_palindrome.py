def is_palindrome(phrase):
    phrase = phrase.lower().replace(" ", '')
    lst = list(phrase)
    reversed_list = list(phrase)
    reversed_list.reverse()
    return True if lst == reversed_list else False

#     normalized = phrase.lower().replace(' ', '')
#     return normalized == normalized[::-1]

#     if lst == reversed_list:
#         return True
#     else:
#         return False 

# Is phrase a palindrome?

#     Return True/False if phrase is a palindrome (same read backwards and
#     forwards).

print(is_palindrome('tacocat'))      
        # True

print(is_palindrome('noon'))     
        # True

print(is_palindrome('robert'))       
        # False

    # Should ignore capitalization/spaces when deciding:

print(is_palindrome('taco cat'))
        # True

print(is_palindrome('Noon'))
        # True
