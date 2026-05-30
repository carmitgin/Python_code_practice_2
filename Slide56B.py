##2.כתוב פונקציה המקבלת מחרוזת ומחזירה את אורכה כפול 2.
##Write a function that receives a string and returns its length multiplied by 2.

def string_length_doubled(s: str) -> int:
    '''this function receives a string and returns its length multiplied by 2.
    
    Args:
        s (str): the string to check
    
    returns:
        int: the length of the string multiplied by 2
    
    Example:
        string_length_doubled("hello") -> 10
    '''
    return len(s) * 2   

text = input("Please enter a string: ")
print("the length of the string multiplied by 2 is: ", string_length_doubled(text))
