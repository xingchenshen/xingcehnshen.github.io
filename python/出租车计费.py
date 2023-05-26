a=float(input("请输入总里程："))
price=0
if a<=0:
  print("错误")
elif a<=3:
   price=10
elif a>3 and a<10:
   price=(a-3)*1.2+10
else:
   price=(a-10)*1.5+22 

print("费用为:{:.1f}".format(price))
