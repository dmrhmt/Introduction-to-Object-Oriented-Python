# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:16:04 2020

@author: demir
"""
# tuples are immutable. It means that you can NOT change it's elements.
lis = [1,2,3]
tupl = (1,2,3) # tuple, also works without brackets
print(lis)
print(tupl)

x,y,z = tupl # unpacking
print(x)
x = 10
# creating new tuple, NOT modifying old one 
tupl = (x,y,z)
print(tupl) # 10,2,3

# below code does NOT work on tuple
#print(tupl[2])
#tupl[2] = 10 

tupl2 = ([1,2,3], [4,5,6]) # it includes list, so operations on list are applicable 
tupl2[0][1] = 1010
print(tupl2)
