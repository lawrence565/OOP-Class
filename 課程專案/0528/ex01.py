#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:21:09 2024

@author: Lawrence
"""

from guess import figure_guess
userPoint = 0

def run():
    userGesture = input("請輸入「剪刀」、「石頭」或「布」？")
    comGesture = figure_guess()
    print('電腦出 ' + comGesture)
    
    if userGesture == '剪刀':
        if comGesture == '石頭':
            print('電腦獲勝')
        elif comGesture == '剪刀':
            print('平手')
        elif comGesture == '布':
            print('玩家獲勝')
            userPoint + 1
    elif userGesture == '石頭':
        if comGesture == '石頭':
            print('平手')
        elif comGesture == '剪刀':
            print('玩家獲勝')
            userPoint + 1
        elif comGesture == '布':
            print('電腦獲勝')
    elif userGesture == '布':
        if comGesture == '石頭':
            print('玩家獲勝')
            userPoint + 1
        elif comGesture == '剪刀':
            print('電腦獲勝')
        elif comGesture == '布':
            print('平手')
    else:
        print('請重新輸入')
        
while (userPoint < 5):
    run()