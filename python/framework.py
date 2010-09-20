"""Implementing a toy unit testing framework in 
Python, employing the introspection mechanisms 
available in the language.

"module" represents the module in which the data is 
present. All the available classes from the
"module" are checked whether they are derived from           
"baseclass". If so, this framework finally calls those 
methods inside them which have their names starting 
with "test".

The locations where the user-defined module and 
baseclass are to be inserted are commented out
intentionally.
"""
import #<your data module>
import types

module = #<your data module>
baseclass = #"<your baseclass>"
class_list, final_c_list = [], []

for i in dir(module):
    if type(getattr(module, i)) == types.ClassType:
        class_list.append(i) 

ref = getattr(module, baseclass)

for i in class_list:
    t = getattr(module, i).__bases__
    if t: 
        if t[0] == ref: final_c_list.append(i)

for i in final_c_list:
    o = getattr(module, i)()
    for j in dir(o):
        if j[0:4] == 'test':
            if type(getattr(o, j)) == types.MethodType:
                getattr(o, j)()
                

