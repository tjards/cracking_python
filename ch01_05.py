#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 17:15:12 2023

@author: tjards

One Away:
    
    Given two strings, check if one is one character different from the other
    
    Assume: no change is also o.k.
    
    Note: don't use "exception driven development like in the previous q's"

"""

def one_away(string1, string2):
    
    # strip the ends
    s1 = string1.strip()
    s2 = string2.strip()
    
    # check lengths:
    if abs(len(s1) - len(s2)) > 1:
        return False
    else:
        flag = False 
        # cross ref each char (will allow one deviation)
        s1_list = list(s1)
        # for each character 
        for i in list(s2):
            # check if its in the other list 
            if i in s1_list:
                # if so, remove it 
                s1_list.remove(str(i))
            else: 
                if flag == True:
                    return False 
                else:
                    flag = True 
    return True 

# terminal call
# -------------
if __name__ == "__main__":
    
    string1 = input("Enter String 1: ")
    string2 = input("Enter String 2: ")
    print(one_away(string1, string2))

