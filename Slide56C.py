def string_count(text: str, char: str) -> bool:
    
    '''this function receives a string and a character, and returns the number of times the character appears in the string
    If the character appears at least 2 times, the function will return True, otherwise it will return False
    
    Args:
        text (str): the string to check
        char (str): the character to count in the string
    
    returns:
        bool: True if the character appears at least 2 times, False otherwise
    
    Example:
        string_count("hello world", "o") -> True
    '''

    count = 0
    for c in text:
     return text.count(text[-1])>1

#text= "this is a test for text for chacking the functions"
text= input("Please enter a string: ")
print("Does the last char appear more than once? ", string_count(text, text[-1]))



