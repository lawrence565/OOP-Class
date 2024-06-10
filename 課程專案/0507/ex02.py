#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:51:46 2024

@author: Lawrence
"""
import sys

studentId = (input("請輸入學號："))
if len(studentId) != 9:
    print("學號格式錯誤")
    sys.exit()

weight = float(input("請輸入體重(Kg)："))
height = float(input("請輸入身高(m)："))
BMI = (weight / (height ** 2))
print(BMI)

if BMI < 18:
    print("體重過輕")
elif BMI < 24:
    print("體重正常")
elif BMI < 27:
    print("體重過重")
elif BMI >= 27:
    print("體重肥胖")
    
    