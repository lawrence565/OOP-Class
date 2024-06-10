#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:34:21 2024

@author: Lawrence
"""
prime_list = []

def find_prime(n):
    for j in range (2, n):
        if (n % j == 0):
            return False
    return True

def find_prime_list(x):
    for i in range(2, x + 1):
        if (find_prime(i)):
            prime_list.append(i)
    return prime_list

x = int(input("請輸入數字："))
find_prime_list(x)
print(f"2 到 {x} 共有 {len(prime_list)} 個質數")
print(prime_list)