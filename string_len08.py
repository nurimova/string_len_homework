def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    a=len(s)-1
    if a%2!=0:
        
        return s[a//2]
    else:
        
        return s[a//2] and s[a//2-1]
s='asdfgh'
print(main(s))