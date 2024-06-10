#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:38:18 2024

@author: Lawrence
"""

import random
import math

class Location:
    def __init__(self):
        self.x = math.floor(random.random() * 10)
        self.y = math.floor(random.random() * 10)
    def move(self):
        self.x = math.floor(random.random() * 10)
        self.y = math.floor(random.random() * 10)
        return (self.x, self.y)
        
class mydata(Location):
    def __init__(self):
        super().__init__()
    def nameAndId(self):
        return '吳秉耀 112054826' 
    
class drugstore(Location):
    def __init__(self):
        super().__init__()
    def count(self):
        return math.floor(random.random() * 1000)
    
def distance(s, p):
    d = math.sqrt((s[0] - p[0]) ** 2 + (s[1] - p[1]) ** 2);
    return d

me = mydata()
s1 = me.move()
print('消費者的資料' + me.nameAndId())
print(f'我的位置：{s1}')
print(" ")
drug = drugstore()
d1 = drug.move()
print(f'剩餘藥劑數量：{drug.count()}')
print(f'藥局的位置：{d1}' )
dis = distance(s1, d1)
print(f'我與藥局之間的距離為：{dis}')