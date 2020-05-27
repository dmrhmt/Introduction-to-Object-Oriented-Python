# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 13:00:56 2020

@author: demir
"""

import fibo
import sys

fibo.fib(5)

print(fibo.fib2(4))

print("filename:")
print(sys.argv[0])

print(fibo.fib2(int(sys.argv[1]))) # to give arg on Spyder, use Ctrl+F6 and select "Command Line Options". Fill the box next to it. !It takes as STRING!
