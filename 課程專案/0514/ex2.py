#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 14:07:58 2024

@author: Lawrence
"""

interestRate = 1 + ((float(input("請輸入年利率：")))/100)
fund = 10000
target = 112054826
year = 0

while fund < target:
    fund *= interestRate
    year += 1

print(f"第 {year} 年後本利和為 {fund} ，超過 {fund - 10000}")