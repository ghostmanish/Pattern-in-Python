# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 16:54:01 2022

@author: mgosh
"""

num = int(input())
for row in range(0,num):
    for col in range(row,-1,-1):
        print(chr(ord('A')+num - 1 - col),end=" ")
    print("\n")