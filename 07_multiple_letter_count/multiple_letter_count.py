def multiple_letter_count(phrase):
    return {letter: phrase.count(letter) for letter in phrase}

    # frequency = {}
    # for letter in phrase:
    #     count = phrase.count(letter)
    #     frequency[letter] = count
    # return frequency
    
# Return dict of {ltr: frequency} from phrase.

print(multiple_letter_count('yay'))
# {'y': 2, 'a': 1}
print(multiple_letter_count('Yay'))
# {'Y': 1, 'a': 1, 'y': 1}