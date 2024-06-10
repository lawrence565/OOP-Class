#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:12:15 2024

@author: Lawrence
"""

import math

cp = int(input('輸入上衣價格：'))
pp = int(input('輸入褲子價格：'))
vp = int(input('輸入背心價格：'))

cq = int(input('輸入上衣數量：'))
pq = int(input('輸入褲子數量：'))
vq = int(input('輸入背心數量：'))

def cal(cp, pp, vp, cq, pq, vq):
    total=  cp * cq + pp * pq + vp * vq
    if total > 1000:
        return math.floor(total * 0.8)
    else:
        return total

print('訂購服裝總金額為 ' + str(cal(cp, pp, vp, cq, pq, vq)))