#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:15:28 2024

@author: Lawrence
"""
import math, random

class Location():
    def __init__(self):
        self.x = math.floor(random.random() * 10)
        self.y = math.floor(random.random() * 10)
        
    def move(self):
        self.x = math.floor(random.random() * 10)
        self.y = math.floor(random.random() * 10)
        return (self.x, self.y)

class Mydata(Location):
    def __init__(self):
        super()
        
    
    def nameAndId(self):
        self.name = "吳秉耀"
        self.id = 112054826
        return(f"{self.name} {self.id}")
    
class Pharmacy(Location):
    def __init__(self):
        super()
    
    def drug(self):
        self.lastDrug = math.floor(random.random() * 1000)
        return self.lastDrug

def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


me = Mydata()
drugStore = Pharmacy()
meLocation = me.move()
storeLocation = drugStore.move()


print("我的資料：" + me.nameAndId())
print("我的位置：" + str(meLocation))
print("快篩剩餘數量：" + str(drugStore.drug()))
print("藥局的位置：" + str(storeLocation)) 
print("我與藥局之間的距離：" + str(distance(meLocation, storeLocation)))

