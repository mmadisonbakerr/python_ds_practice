def number_compare(a, b):
    if a == b:
        print('Numbers are equal')
    elif a < b:
        print('Second is greater')
    elif a > b:
        print('First is greater')

# Report on whether a>b, b>a, or b==a
    
number_compare(1, 1)
        # 'Numbers are equal'
        
number_compare(-1, 1)
        # 'Second is greater'
        
number_compare(1, -2)
        # 'First is greater'