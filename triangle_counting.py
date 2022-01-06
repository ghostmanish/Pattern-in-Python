# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 14:44:20 2022

@author: mgosh
"""

n = int(input())
row = 1
count = 0
while(row<=n):
    col = 1
    while(col<=row):
        count+=1
        print(count,end=" ")
        col+=1
    row+=1
    print("\n")