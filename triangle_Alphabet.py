# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 15:59:44 2022

@author: mgosh
"""

num = int(input())
for row in range(0,num):
    for col in range(0,row+1):
        print(chr(ord('A')+ row + col),end=" ")
    print("\n")