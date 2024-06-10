#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:34:21 2024

@author: Lawrence
"""

def gcd(m, n):
    r = n % m   
    print(f"{m} 與 {n} 的最大公因數相當於 {r} 與 {m} 的最大公因數")
    if r == 0:
        return n/m
    else:
        gcd(r, m)
        return r
        
m = int(input("請輸入 ｍ 值: "))
n = int(input("請輸入 n 值: "))

ans = gcd(m, n)
print(f"{m} 與 {n} 的最大公因數為 {ans}")