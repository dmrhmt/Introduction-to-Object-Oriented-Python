# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:28:29 2020

@author: demir
"""

# key-value pairs
l = [1,18,3,2,12]
print(l[3]) # index is like key, l[3] is like value

tel = {"jack":4098, "sape": 4139}
print(tel["jack"]) # = 4098

d = dict([("sape", 4139), ("guido", 4100), ("jack", 4098)])
print(d["guido"])

for k,v in d.items():
    print(k,v)
    
print([(key,val) for key,val in d.items()])

# ENUMERATE : limiting items in dicts

print((1, 2, 3)              < (1, 2, 4)) # 3<4 True
print([1, 3, 3]              < [1, 2, 4]) # 3!<2 False
print('ABC' < 'C' < 'Pascal' < 'Python') # ascii
print((1, 2, 3, 4)           < (1, 2, 4)) # 3<4 True
print((1, 2)                 < (1, 2, -1)) # nothing<integer True
print((1, 2, 3)             == (1.0, 2.0, 3.0)) #int=float True
print((1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)) # aa<abc True