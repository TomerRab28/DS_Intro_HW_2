# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 23:38:31 2022

@author: USER
"""

def reverse(sentence, reverse_word):
    if not isinstance(reverse_word,str):
       return "invalid input"
    ls =  sentence.split()
    if reverse_word not in ls:
   
    
        return "The word was not found"  
    return (sentence.replace(reverse_word, reverse_word[::-1], 1))
    
a = reverse('acs bnf mop', 33)
print(a)
      
 