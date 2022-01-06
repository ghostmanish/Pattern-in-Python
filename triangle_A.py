# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 14:46:58 2022

@author: mgosh
"""

n = int(input())
row = 1

while(row<=n):
    col = 1
    while(col<=row):
        print("A",end=" ")
        col+=1
    row+=1
    print("\n")