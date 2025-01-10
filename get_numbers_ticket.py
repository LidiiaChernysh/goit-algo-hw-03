import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:

    """ 
    The function generates a set of unique random numbers 
    in a given range and returns a list of randomly selected, sorted numbers.
    If the parameters do not meet the specified constraints, 
    the function returns an empty list.

    Parameters:
        min (int): the minimum possible number in the set (not less than 1).
        max (int): the maximum possible number in the set (not more than 1000).
        quantity (int): the number of numbers to choose (a value between min and max).

    Returns:
        list: a list of randomly selected, sorted numbers or an empty list
        empty list: if the parameters do not meet the specified constraints
    """

    if ((1 <= min) 
        and (max <= 1000) 
        and (min <= quantity <= max - min)):
        list_numbers = random.sample(range(min, max+1), quantity)
        list_numbers_sorted = sorted(list_numbers)
        return list_numbers_sorted
    else:
        return []

    
print(get_numbers_ticket(10,1000,990))

