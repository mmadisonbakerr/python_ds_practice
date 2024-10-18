def calculate(operation, a, b, make_int=False, message='The result is'):
    if operation == 'add':
        sum = a + b
    elif operation == 'subtract':
        sum = a - b
    elif operation == 'multiply':
        sum = a * b
    elif operation == 'divide':
        sum = a / b
    if make_int == True:
        print(message, int(sum))
    else: 
        print(message,sum)

    #         if make_int:
    #     res = int(res)

    # return f"{message} {res}"
        
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> 
        'The result is 6.5'

        >>> 
        'The result is 2'

        >>> 
        'The result is 3.0'

        >>> 
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)
        
    """
(calculate('add', 2.5, 4))

(calculate('subtract', 4, 1.5, make_int=True))

(calculate('multiply', 1.5, 2))

(calculate('divide', 10, 4, message='I got'))