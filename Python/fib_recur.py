
#### PYTHON RECURSION LIMIT IS 46765 ####
####   UNLESS YOU SET IT OTHERWISE   ####

####   Implementing MEMOIZATION to   ####
####       make fib(n) faster        ####
def memoized_fib(x):
    if values.has_key(x): 
        return values[x]
    else: 
        values[x] = fib(x)
        return values[x]   


def fib(n):   
    if n == 0: return 0
    elif n == 1: return 1
    else: return memoized_fib(n-2) + memoized_fib(n-1)


values = {0: 0, 1: 1}     
