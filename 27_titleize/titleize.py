def titleize(phrase):
    return ' '.join([word.capitalize() for word in phrase.lower().split()])

# return phrase.title()

    # phrase = phrase.lower()
#     new_phrase = []
#     new_phrase = " ".join(new_phrase)
#     print(new_phrase)

    # phrase = phrase.lower()
    # phrase = phrase.split()
    # new_phrase = []
    # for word in phrase:
    #     new_phrase.append(word.capitalize())
    # new_phrase = " ".join(new_phrase)
    # print(new_phrase)

    """Return phrase in title case (each word capitalized)."""

print(titleize('this is awesome'))
        # 'This Is Awesome'

print(titleize('oNLy cAPITALIZe fIRSt'))
        # 'Only Capitalize First'
    
