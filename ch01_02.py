#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 14:25:33 2023

@author: tjards

Check Permutation:
    
    Given two strings, write a method to determine if one is a 
    permutation of another
    
    assume case senstive


"""

# check permutation function
# --------------------------
def check_permutation(string1, string2):
    
    # let's remove spaces... etc
    s1 = ''.join(string1.split())
    s2 = ''.join(string2.split())
    
    # first, they must be the same length
    if len(s1) != len(s2):
        return False
    # more complicated check
    else:
        # convert s2 to a list
        s2_list = list(s2)
        # incremental remove each character
        for i in list(s1):
            # try to remove
            try:
                s2_list.remove(str(i))
            # if you can't, it means its not there
            except:
                return False
    return True



# terminal call
# -------------
if __name__ == "__main__":
    
    string1 = input("Enter string 1: ")
    string2 = input("Enter string 2: ")
    print(check_permutation(string1, string2))