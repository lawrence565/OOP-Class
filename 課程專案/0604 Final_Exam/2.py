#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:15:26 2024

@author: Lawrence
"""
import sys


stdId = input("請輸入學號：")
if len(stdId) != 9:
    print("學號格式錯誤")
    sys.exit()
    
def calBMI():
    w = float(input("請輸入體重（KG）："))
    l = float(input("請輸入體重（m）："))
    
    bmi = w / (l ** 2)
    print("BMI = " + str(bmi))
    
    if bmi < 18:
        print("體重過輕")
    elif bmi < 24:
        print("體重正常")
    elif bmi < 27:
        print("體重過重")
    else:
        print("體重肥胖")
        
calBMI()