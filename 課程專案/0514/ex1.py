#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:35:47 2024

@author: Lawrence
"""
import sys

studentid = tuple(input("請輸入學號："))
existingChar = {}

if len(studentid) != 9:
    print("學號錯誤")
    sys.exit()

for char in studentid:
        if char not in existingChar:
            existingChar[char] = 1
        else:
            existingChar[char] += 1

for char, count in existingChar.items():
    print(f"{char} 共出現 {count} 次")