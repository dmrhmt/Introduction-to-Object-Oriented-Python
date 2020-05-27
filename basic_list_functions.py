# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:12:43 2020

@author: demir
"""

l = [1,2,3,4]
print(l)
l.append(55) # adds 55 to end
print(l)
l.insert(2, 111) # adds 111 to 3. position
print(l)
l.append(111)
print(l)
l.remove(111) # removes first 111
print(l)
print(l.pop()) # pops last element of list, prints it
print(l)
print("pop(0)")
print(l.pop(0)) # pops 0th element of list, prints it
print(l.index(4)) # locate 4 in list
print(l.count(3)) # count the number of 3
l.append(0)
print(l)
l.sort() # sorts the list
print(l)

l2 = [9,11,13]
l_copy = l
l.extend(l2) # adds l2 to the end of l 
print(l)

"""as shown below, the difference between append a list to list 
 and extend is appends adds the list to the other as the second list's element,
 extend adds every element of l2 to the end of l1 """

l_copy.append(l2)
print(l_copy)

# l_copy.sort() """ sort does NOT work between list and int! """

l_copy.clear() # clears the list
print(l_copy)

# shallow copy vs deep copy: shallow = pointer reference, deep = element copy

# shallow copy (pointer)

l_copy.append(300)
l3 = l_copy # only 300 is inside of l_copy and l3
l_copy.append(600)
print(l_copy)
print(l3) # l3 has 600 also

# deep copy
l4 = l_copy.copy() # both has 300 and 600
l_copy.append(700)
print(l_copy) # 300,600,700
print(l4) # 300, 600

