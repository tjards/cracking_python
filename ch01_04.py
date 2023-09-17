#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 16:22:47 2023

@author: tjards

Palindrome permutation:
    
    Given a string, check to see if it is a permutation of a palindrome
    

"""

# function 
# --------
def palindrome_permutation(string):
    
    # strip the ends off
    s = string.strip()
    
    # convert to a list 
    s_list = list(s)
    
    # if the length is even, then all letters must have a pair
    if len(s_list)%2 == 0:
        # search each letter
        for i in s_list:
            # remove one
            s_list.remove(str(i))
            try:
                # remove another
                s_list.remove(str(i))
            except:
                return False
            
    # if the length is odd
    else:
        # set a flag 
        Flag = False
        # now search through list
        for i in s_list:
            # remove one
            s_list.remove(str(i))
            try:
                # remove another 
                s_list.remove(str(i))
            # if you can't, that's our only permitted loner
            except:
                # if we already have a flag
                if Flag == True:
                    # then it can't be palindrom
                    return False
                else:
                    # keep searching
                    Flag = True
                    print("center of palindrome: ",i)
    return True 


# terminal call
# -------------
if __name__ == "__main__":
    
    string = input("enter string: ")
    print(palindrome_permutation(string))