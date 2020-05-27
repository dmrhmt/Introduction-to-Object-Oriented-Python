# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:26:28 2020

@author: demir
"""

l = [1,2,3]
l.append(23)
print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)

l2 = [44, 33, 22]
l2.append(11)
print(l2)
print(l2.pop(0)) # pops 0th element of l2
print(l2)
from collections import deque

l3 = deque([33,22])
print(l3) # it is not list, it is "deque([33, 22])". (object oriented type)
l3.append(67)
print(l3.popleft())
print(l3) # = deque([22, 67])