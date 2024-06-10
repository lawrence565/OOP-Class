#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:42:10 2024

@author: Lawrence
"""

id = input("請輸入學號：")
myId = "112054826"

if (id == myId):
    print("本人")   
elif (id[0:7] == myId[0:7]):
    print("同年級 同科系 同班")    
elif (id[0:5] == myId[0:5]):
    print("同年級 同科系")
elif (id[0:3] == myId[0:3]):
    print("同年級")
else:
    print("非同年級生")