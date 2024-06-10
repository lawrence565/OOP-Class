#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:08:06 2024

@author: Lawrence
"""

people = {"01": "王大明", "02": "蔡曉慧", "112054826": "吳秉耀"}

keys = []
for key in people.keys(): keys.append(key)

print("可輸入學號： dict_keys[", keys, "]")
print(people)

looking = input("\n請輸入查詢學號：")
if (looking in keys) : data = people[looking]
else: data = "字典找不到該學號"

print("對應姓名為：", data)