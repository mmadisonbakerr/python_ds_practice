def repeat(phrase, num):
    if isinstance(num, int) == False or num < 0: 
        return None
    elif num == 0:
        return ''
    elif isinstance(num, int) == True:
        return phrase * num
    
    #    if not isinstance(num, int) or num < 0:
    #     return None

    # return phrase * num

    """Return phrase, repeated num times.

        >>> 
        '***'

        >>> 
        'abcabc'

        >>> 
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
print(repeat('*', 3))
print(repeat('abc', 2))
print(repeat('abc', 0))
print(repeat('abc', -1))
print(repeat('abc', 'nope'))