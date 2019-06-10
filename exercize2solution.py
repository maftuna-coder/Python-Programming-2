# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 15:05:09 2019

@author: Maftuna
"""

print ("Logic gate simulation program")

def AND (a,b,c):

    a = int(a)
    b = int(b)
    c = str('AND')
    if a == 1 and b == 1:
        return 1
    else:
        return 0


def OR(a,b,c):
    a = int(a)
    b = int(b)
    c = str('OR')
    if a == 1:
        return 1
    elif b == 1:
        return 1
    else:
        return 0


def NOT (a,b,c):
    a = int(a)
    b = int(b)
    c = str('NOT')
    if a == 0:
        return 1
    else:
        return 0

def Main():
    c = input("what type of gate do you want to simulate - OR, AND  or NOT?  ") 
    a = input("enter value for first input ->  ")
    b = input("enter value for second input ->  ")
    
    if c == 'AND':
        x = AND(a,b,c)
        print ("Output of {} AND {} is {}".format(a, b, x))
        
    if c == 'OR':
        x = OR(a,b,c)
        print ("Output of {} OR {} is {}".format(a,b,x))
        
    if c == 'NOT':
        x = NOT(a,b,c)
        print ("Output of NOT {} is {}".format(a, x))
        
    else:
        print("")
    
              
Main()