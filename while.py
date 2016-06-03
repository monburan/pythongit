#coding:UTF-8
#while循环
#与前面的if一样，过缩进的方法区别不同的代码
#首先定义一个变量i
#通过while语句显示i从0到6的过程
i = 0
while (i < 6):
    print "%d - -> %d"%(i,i+1)
    i += 1
#在while语句中也可以含有if语句
while (i < 6):
    if(i+1==6):
        print "%d -/-> 6"%(i)
    else:
        print "%d - -> %d"%(i,i+1)
    i += 1
#这样在5到6的时候就会显示5-/->6