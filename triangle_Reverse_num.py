# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 14:44:50 2022

@author: mgosh
"""

n = int(input())
row = 1
count = 15
while(row<=n):
    col = 1
    while(col<=row):
        
        print(count,end=" ")
        count-=1
        col+=1
    row+=1
    print("\n")