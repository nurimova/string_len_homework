def main(s1,s2):
    """
    Given two strings, s1 and s2. Find their total length.
    Args:
        s1: string
        s2: string
    Returns:
        total length of strings
    """
    x1=len(s1)
    x2=len(s2)
    return x1+x2
s1='asdfg'
s2='qwert'
print(main(s1,s2))