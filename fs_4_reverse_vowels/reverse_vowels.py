def reverse_vowels(s):
    vowels = set("aeiou")

    string = list(s)
    i = 0
    j = len(s) - 1

    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1

    return "".join(string)

    # s = list(s)
    # vowel_removed = []
    # vowels = 'aeiou'
    # for char in s:
    #     if char in vowels:
    #         vowel_removed.append(char)
    #         vowels[char] = '*'
    # vowel_removed.reverse()
    # for char in s:
    #     if char == '*':
    #         s[char] = vowel_removed[char]
    # return s 

    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order. """

print(reverse_vowels("Hello!"))
    # 'Holle!'

print(reverse_vowels("Tomatoes"))
    # 'Temotaos'

print(reverse_vowels("Reverse Vowels In A String"))
    # 'RivArsI Vewols en e Streng'

print(reverse_vowels("aeiou"))
    # 'uoiea'

print(reverse_vowels("why try, shy fly?"))
    # 'why try, shy fly?''
   