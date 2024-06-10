# -*- coding: utf-8 -*-

personalData = []
personalData.append(input("請輸入科系："))
personalData.append(input("請輸入班級："))
personalData.append(input("請輸入學號前三碼："))
personalData.append(input("請輸入學號後六碼："))
personalData.append(input("請輸入姓名："))

data1 = personalData[0]
personalData.pop(0)
data2 = personalData[0]
personalData.pop(0)

print(data1, data2, personalData)

data3 = personalData[-1]
personalData.pop()

print(data3, personalData)
