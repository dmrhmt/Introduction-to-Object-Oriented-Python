# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:46:57 2020

@author: demir
"""

s = {1,2,3} # a set

# In sets, ORDER IS NOT IMPORTANT!
k = {9,9,9,9}
print(s) # = {1,2,3}
print(k) # = {9}

k2 = set(s)
k3 = set([1,2,3,1,32,3])
print(k2)
print(k3)

k4 = set("bilgisayarkavramlari")
k5 = set("ahmetDemir")
print(k4)
print(k5)

print(k4|k5) # UNION OPERATOR

print(k3-k2) # SET DIFFECENCE

print(k2&k3) # INTERSECTION

print(k2^k3) # XOR 