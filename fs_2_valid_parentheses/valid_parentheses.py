def valid_parentheses(parens):
    parens = list(parens)
    if parens[0] == ')' or parens[-1] == '(':
        return False
    return True if len(parens) % 2 == 0 else False

    count = 0

#     for p in parens:
#         if p == '(':
#             count += 1
#         elif p == ')':
#             count -= 1

#         # fast fail: too many right parens
#         if count < 0:
#             return False


    """Are the parentheses validly balanced?"""

print(valid_parentheses("()"))
        # True

print(valid_parentheses("()()"))
        # True

print(valid_parentheses("(()())"))
        # True

print(valid_parentheses(")()"))
        # False

print(valid_parentheses("())"))
        # False

print(valid_parentheses("((())"))
        # False

print(valid_parentheses(")()("))
        # False