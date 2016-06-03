#coding:UTF-8

#python和我之前学习的c/c++/c#都有所不同
#尤其是在写一些语句的时候，python编写格式对我之前所学的知识有太大冲击了
#python中没有了大括号，没有了分号，全部通过缩进来进行，非常简洁

i = raw_input()
#if语句
#if (int(i)<2):
#    print "%d < 2"%(int(i))
#else:
#    print "%d > 2"%(int(i))
#没有了大括号，看起来很清爽
#通过键盘输入一个数让程序判断是否大于或小于
#我们输入一个1，程序返回了 1<2
#输入了一个2程序返回的结果是 2>2，很明显这和我们思维中想象的是不一样的...
#但是万一输入的数字等于2呢？
#if语句还可以这样写
if (int(i)==2):
    print "%d = 2"%(int(i))
elif (int(i)!=2):
    if (int(i)<2):
        print "%d < 2"%(int(i))
    else:
        print "%d > 2"%(int(i))
#在elif那里注意一定要与上面的if对齐，不然系统会报错SyntaxError: invalid syntax