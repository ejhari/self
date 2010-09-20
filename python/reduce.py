
def reduce (f, s, i=None):
    """My own implementation of built-in reduce(). 

    f is the function that must work on the 
    adjacent elements in the sequence s.
    If initial i is given, it is placed before
    the sequence, or becomes the default if an
    empty sequence is passed."""

    if i is not None: s.insert(0,i)

    ans, j = s[0], 1

    while j < len(s):
        ans, j = f(ans,s[j]), j+1
    
    return ans


