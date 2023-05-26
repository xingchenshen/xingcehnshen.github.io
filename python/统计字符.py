import string
s=input("请输入字符串:")
zimu=0
shuzi=0
kongge=0
qita=0
i=0
for t in s:  
     if t.isalpha():
        zimu=zimu+1
     elif t.isdigit():
        shuzi=shuzi+1
     elif t==" ":
        kongge=kongge+1
     else:
        qita=qita+1
print("字母：{}，数字{}，空格{}，其他{}".format(zimu,shuzi,kongge,qita))
