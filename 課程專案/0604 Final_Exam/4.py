#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:15:27 2024

@author: Lawrence
"""

import guess

userPoint = 0
comPoint = 0
roundCount = 1
gesture = ["剪刀", "石頭", "布"]

while (userPoint < 2):
    print(f"第{roundCount}局：")
    userGes = input("輸入剪刀石頭布其中一種：")
    if userGes not in gesture:
        print("輸入錯誤請再試一次")
        roundCount += 1
        continue
    comGes = guess.guessGes()
    print("電腦出 " + comGes)
    
    if userGes == "剪刀":
        if comGes == "剪刀":
            print("平手")
        elif comGes == "石頭":
            print("電腦獲勝")
            comPoint += 1
        elif comGes == "布":
            print("玩家獲勝")
            userPoint += 1
    elif userGes == "石頭":
        if comGes == "剪刀":
            print("玩家獲勝")
            userPoint += 1
        elif comGes == "石頭":
            print("平手")
        elif comGes == "布":
            print("電腦獲勝")
            comPoint += 1
    elif userGes == "布":
        if comGes == "剪刀":
            print("電腦獲勝")
            comPoint += 1
        elif comGes == "石頭":
            print("玩家獲勝")
            userPoint += 1
        elif comGes == "布":
            print("平手")
    
    print(f"電腦 vs 玩家 {comPoint} : {userPoint}")
    roundCount += 1
    if (comPoint == 2):
        break

if userPoint == 2:
    print("最終結果：玩家勝")
elif comPoint == 2:
    print("最終結果：電腦勝")

