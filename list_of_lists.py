# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 19:51:11 2020

@author: demir
"""

l = [0,1,2]
m = [[3,4,5], [9,10,11], [6,7,8], l] # remember! shallow copy
print(m)

transpose = [[row[i] for row in m] for i in range(3)]
print(transpose)
print(len(transpose))

del(m[1])
print(m)