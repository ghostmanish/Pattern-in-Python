# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 13:28:33 2022

@author: mgosh
"""

n = int(input())
i = 0

while(i<n):
    j = 0
    while(j<n):
        print("*",end=" ")
        j+=1
    i+=1
    print("\n")