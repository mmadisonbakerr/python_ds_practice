def single_letter_count(word, letter):    
    return word.lower().count(letter) 
    

    # char = 0
    # lowercase_word = word.lower()
    # for letters in lowercase_word:
    #     if letter in lowercase_word:
    #         char += 1
    # return char 
    
    
# How many times does letter appear in word (case-insensitively)?

print(single_letter_count('Hello World', 'z'))
# 0
print(single_letter_count('Hello World', 'h'))
# 1
print(single_letter_count("Hello World", 'l'))
# 3