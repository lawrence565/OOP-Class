#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:15:27 2024

@author: Lawrence
"""
import math

ran = int(input("請輸入範圍："))
prime = []

def checkPrime(i):
    lim = math.floor(math.sqrt(i)) + 1
    for j in range(2, lim+1):
        if (i % j == 0):
            if j != i:
                break
            else:
                prime.append(i) 
        else:
            if j == lim:
                prime.append(i)
        
for i in range(2, ran):
    checkPrime(i)
    
            
print(prime)