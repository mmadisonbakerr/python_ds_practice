def vowel_count(phrase):
    phrase = phrase.lower()
    vowel = 'aeiou'
    return {char: phrase.count(char) for char in phrase if char in vowel}
    
    # for char in phrase:
    #     if char in vowel:
    #         count = phrase.count(char)
    #         frequency[char] = count
    # print(frequency) 

    """Return frequency map of vowels, case-insensitive. """

print(vowel_count('rithm school'))
        # {'i': 1, 'o': 2}
        
print(vowel_count('HOW ARE YOU? i am great!'))
        # {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
   