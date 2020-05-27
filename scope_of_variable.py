# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:07:21 2020

@author: demir
"""

def scope_test():
    def do_local():
        spam = "local spam"
        print("print inside do local function:" + spam)

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)