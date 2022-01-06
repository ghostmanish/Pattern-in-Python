# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 14:40:25 2022

@author: mgosh
"""

n = int(input())
row = 1

while(row<=n):
    col = 1
    while(col<=row):
        
        print(col,end=" ")
        col+=1
    row+=1
    print("\n")