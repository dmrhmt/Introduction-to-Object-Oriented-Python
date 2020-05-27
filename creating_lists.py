# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:33:40 2020

@author: demir
"""
# From there 
l = []
for x in range(1,10):
    l.append(x**2)
print("x:")
print(x)
print("l:")
print(l)
""" to there the code has side effect(s). The code should NOT do something else than what is wanted.
 x variable can be accessed outside from loop.
 It is NOT what was intented.
"""
# the first parameter of map func. is a function to apply, 2nd parameter is a list
squares = list(map(lambda y: y**2, range(10))) # in here, map means "apply the lambda function to all over the list(0,9)"
print(squares)
#print(y) """name 'y' is not defined """


def f(x):
    return x+10
l2 = [3,4,5]
print(list(map(f,l2)))

squares2 = [z**2 for z in range (20)]
print(squares2)
#print(z) """no side effect """ 

l4 = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(l4)

l5 = [(x,y,z) for x in [1,2,3] for y,z in [(1,2),(2,3),(3,4)] if x != y]
print(l5)

l6 = [(x,y,z,t) for x in range(1,10) for y in range(x+1, x+2) for z in range(x+2, x+3) for t in range(x+3, x+4)]
print("l6\n\n")
print(l6)