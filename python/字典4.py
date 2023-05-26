dstr=input("请输入字符串：")
print("出现了{}种字符".format(len(set(dstr))))
dict_num={}
for ch in dstr:
    if ch.isupper() or ch.islower():
        dict_num[ch]=dict_num.get(ch,0)+1
    dstr_list=list(dict_num.items())
    dstr_list=sorted(dstr_list,key=lambda x:x[1],reverse=True)
count=0
for ch,num in dstr_list:
        count=count+1
        print("{}:{}".format(ch,num))
        if count>=5:
            break    
        
