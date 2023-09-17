#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 14:52:23 2023

@author: tjards

URLIFY:
    
    Write a method to replace all spaces in string with '%20'. 

"""

# function
# ---------

def urlify(string):
    
    # strip the ends off and replace, add some stuff
    s = "http://www." + string.strip().replace(" ","%20") + ".com"
    return s

# terminal call
# -------------
if __name__ == "__main__":
    
    string = input("Enter string 1: ")
    print(urlify(string))