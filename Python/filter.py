
def filter (f,l):
    """My own implementation of built-in filter()

    f is the function which must work on
    the input sequence l.
    If type of l is tuple or string, return
    sequence is of same type. Otherwise, it
    is converted to list type.""" 

    ans, i = [], 0
    
    while i < len(l):
        if f is None: 
            if l[i]: ans.append(l[i]) 
        elif f(l[i]): ans.append(l[i])  
        i+=1  
 
    if type(l) is tuple or str: return ans   
    else: return list(ans)

