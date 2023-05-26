import random
a=random.randint(1,100)
count=0
while True:
    try:
        n=eval(input("请输入："))
        if type(n) :
            print("输入错误，必须输入整数！")
            print("请重新输入整数:")
            continue
        else:
            count=count+1
            if n==a:
                print("恭喜你，答对了！")
                print("预测了{}次，你猜中了！".format(count))
                break
            elif n>a:
                print("猜的有点大")
            else:
                print("猜的有点小")
     
    except:
          print("输入格式错误，结束程序！")
          break
        
    
        
    
   
       
