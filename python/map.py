
def map (f,*l):
    """Implementation of built-in map() in my own way

    f is the function to be mapped to the corresponding
    elements of each argument. The arguments passed are
    received by l."""

    ans, temp, i = [], [], 0
 
    for arg in l:
        if len(arg) != len(l[0]):
            raise IOError('Unequal argument lists !!!')

    while i < len(l[0]):
        for j in range(0, len(l)):
	     temp.append(l[j][i])
        ans.append(f(*temp))
	temp, i = [], i+1

    return ans

