# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 14:51:47 2022

@author: mgosh
"""

n = int(input())
for  row in range(1,n+1):
    for col in range(row,0,-1):
        print(col,end="")
    print("\n")