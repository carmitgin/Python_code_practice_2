

def num_count(num1: int) -> int:
    '''this function receives an integers and returns the number multipled by 2. Then prints the multiplied number. 
    Args:
        num1 (int): the integer to multiply by 2
    
    returns:
        str: "the multiplied number is"
    
    Example:
        "the multiple number is: 10" if the input is 5
    '''

    result = num1 * 2
    print("the multiplied number is:", result)
    return result

number = int(input("Please enter an integer: "))
num_count(number)
print("the multiplied number is:", num_count(number))


