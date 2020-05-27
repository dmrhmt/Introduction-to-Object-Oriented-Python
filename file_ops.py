# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 13:24:07 2020

@author: demir
"""

file = open("bilgisayar.txt", "w")
file.write("bilgisayar\tKavramlari\n")
file.close()

file = open("bilgisayar.txt", "r")
text = file.read()
file.close()
print(text)
