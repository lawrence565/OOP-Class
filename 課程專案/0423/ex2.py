base = int(input("請輸入本金："))
interest = 1 + (float(input("請輸入利率：")) * 0.01)
res = base * interest
print("第一年本立和為" + str(res))
res = base * (interest ** 2)
print("第二年本立和為" + str(res))
res = base * (interest ** 3)
print("第三年本立和為" + str(res))
