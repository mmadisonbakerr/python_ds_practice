def flip_case(phrase, to_swap):
    new_phrase = []
    for letter in phrase: 
        if letter.islower() == True and letter.lower() == to_swap.lower(): 
            new_phrase.append(letter.upper())
        elif letter.isupper() == True and letter.lower() == to_swap.lower():
            new_phrase.append(letter.lower())
        else:
            new_phrase.append(letter)
    return ''.join(new_phrase)

#     to_swap = to_swap.lower()
#     out = ""

#     for ltr in phrase:
#         if ltr.lower() == to_swap:
#             ltr = ltr.swapcase()
#         out += ltr

#     return out

# # Flip [to_swap] case each time it appears in phrase.

print(flip_case('Aaaahhh', 'a'))      
        # 'aAAAhhh'

print(flip_case('Aaaahhh', 'A'))      
        # 'aAAAhhh'

print(flip_case('Aaaahhh', 'h'))      
        # 'AaaaHHH'


