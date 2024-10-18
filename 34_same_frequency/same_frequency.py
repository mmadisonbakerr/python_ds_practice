def same_frequency(num1, num2):
    num1 = list(map(int, str(num1)))
    num2 = list(map(int, str(num2)))
    return True if sorted(num1) == sorted(num2) else False


    
# Do these nums have same frequencies of digits?
    
print(same_frequency(551122, 221515))        
        # True
        
print(same_frequency(321142, 3212215))       
        # False
        
print(same_frequency(1212, 2211))       
        # True
