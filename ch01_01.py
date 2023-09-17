#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 10:31:15 2023

@author: tjards

Implement an algo to determine if a string has all unique characters

What if you cannot use additional data structures?

"""

# uniqueness function
# -------------------
def isunique(s):
    
    # we assume ascii, so check that it is
    if len(s.encode('ascii')) != len(s):
        raise Exception("You must enter acsii characters")
    
    # remove white space, tabs... etc
    s = ''.join(s.split())
    print('Testing this string: ',s)
        
    # since acsii has 128 characters, if we have more, we know non-uniqueness
    if len(s) > 128:
        return False
    # now we will search through
    else:
        #create an empty set
        char_set= set()
        # search through each
        for i in s:
            # if it is in the set
            if i in char_set:
                return False
            else:
                # add it to the set
                char_set.add(i)
    return True
  
                
# run it
# -----   
string_input = str("This is the non-unique string") 
print(isunique(string_input))
string_input = str("  a b c d e f 1! 3 4 5 u q   ") 
print(isunique(string_input))