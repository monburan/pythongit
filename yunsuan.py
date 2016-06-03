#coding:UTF-8

#我们了解一下python的运算符
#首先是常用的加减乘除
print 2+2
print 2*3
print 2-3
print 4/2
#运算结果分别是 4 6 -1 2，这很容易理解
print 2*2+3
#运行结果为7，这里我们看到，python里面是先运行乘法再运行加法,乘法的优先级高于加法
print 3**4
#运行结果为81，**表示乘方，上面的公式表示3的4次方
print 2*3-3**3
#运行结果为-21，在这条语句中进行计算的优先级为**>*>-
#常用的比较运算符
print 2<4
print 2==4
print 2>4
#运行结果分别是true,false,false，三个符号对应小于等于大于
print 2<=1
print 2<=2
print 2<=4
#运行结果分别是false，true，true，<=代表小于等于，同理可以写出小于等于
print 2!=3
#运行结果是true，!=代表不等于
#逻辑运算符，通过逻辑运算符可以将多个表达式结合到一起，运算后得到的结果是一个布尔值
print 2>4 and 2>3
print 2>4 or 2<4
print not 3>4
#运行结果是false，true，true，and，or，not分别代表与或非