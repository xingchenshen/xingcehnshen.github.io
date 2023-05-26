dic_repertory={"酱油":50,"醋":60,"盐":100,"糖":120,"鸡精":20,"麻油":40}
dic_repertory["酱油"]=100
dic_repertory["醋"]=80
dic_repertory["鸡精"]=50
dic_repertory["耗油"]=60
print(dic_repertory)
print("按食品库存数量排序后为：")
print(sorted(dic_repertory.items(),key=lambda x:x[1] ,reverse=True))

qian={"酱油":50*5,"醋":60*6,"盐":100*1,"糖":120*12,"鸡精":20*2,"麻油":40*10,"耗油":60*6}
print(max(qian))
print(min(qian))
