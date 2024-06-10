shirt = 300
pants = 350
vest = 400
short_num = int(input("請輸入上衣數量："))
pants_num = int(input("請輸入褲子數量："))
vests_num = int(input("請輸入背心數量："))
print("訂購服裝的總金額為：" + str((shirt * short_num) + (pants * pants_num) + (vest * vests_num)))

