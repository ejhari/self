
from listops import *

def element(a, b):
    if null(a): return False
    elif b == first(a): return True
    else: return element(rest(a), b)

def append(a, b):
    if null(a) and null(b): return []
    elif not null(a): return cons(first(a), []) + append(rest(a), b)
    elif not null(b): return cons(first(b), []) + append(a, rest(b))

def reverse(a):
    if null(a): return []
    else: return append(reverse(rest(a)), [first(a)])

def intersection(a, b):
    if null(a): return []
    elif element(b, first(a)): 
        return append([first(a)], intersection(rest(a), b))
    else: return intersection(rest(a), b)

def flatten(a):
    if null(a): return []
    elif type(first(a)) == type([]):
        return append(append(first(a), []), flatten(rest(a)))
    else: return append ([first(a)], flatten(rest(a)))

def maximum(a, b):
    if null(a): return b
    elif first(a) > b: return maximum(rest(a), first(a))
    else: return maximum(rest(a), b)


