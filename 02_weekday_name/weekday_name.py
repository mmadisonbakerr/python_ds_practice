def weekday_name(day_of_week):
    if day_of_week == 1:
        return "Sunday"
    elif day_of_week == 2:
        return "Monday"
    elif day_of_week == 3:
        return "Tuesday"
    elif day_of_week == 4:
        return "Wednesday"
    elif day_of_week == 5:
        return "Thursdau"
    elif day_of_week == 6:
        return "Friday"
    elif day_of_week == 7:
        return "Saturday"
    else:
        return None
    
    #     DAYS = [
    #     "Sunday",
    #     "Monday",
    #     "Tuesday",
    #     "Wednesday",
    #     "Thursday",
    #     "Friday",
    #     "Saturday",
    # ]

    # if day_of_week < 1 or day_of_week > 7:
    #     return None

    # return DAYS[day_of_week - 1]

    """Return name of weekday.
    
        >>> 
        'Sunday'
        
        >>> 
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> 
        >>> weekday_name(0)
    """

print(weekday_name(1))
print(weekday_name(7))
print(weekday_name(9))

