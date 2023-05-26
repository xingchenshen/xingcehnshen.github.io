import random
A=[]
for i in range(10):
    A.append(random.randint(2,100))
print("生成的列表A为：",end="")
print(A)
B=[]
for i in A:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        B.append(i)
c=len(B)
print("一共有{}个素数:".format(c),end="")
print(B)
      
      
      
