# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 15:35:32 2022

@author: mgosh
"""

num = int(input())

row = 1
while(row<= num):
    col = 0
    while(col<num):
        print(chr(ord('A')+col),end=" ")
        col += 1
    row += 1
    print("\n")