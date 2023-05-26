import random
who=["小马","小羊","小兔","小鹿"]
where=["草地上","在家里","电影院","在学校"]
what=["看电影","听故事","吃完饭","做作业"]
who.append("小猫")
where.append("在超市")
what.append("买玩具")
a=random.randint(0,4)
b=random.randint(0,4)
c=random.randint(0,4)
print("新造的句子是：",end="")
print(who[a],end="")
print(where[b],end="")
print(what[c])
