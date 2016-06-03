#coding:UTF-8
#上面那行是为了下面的注释中中文的出现做准备
print 'Hello world!'
#首先我们先输出所有语言的第一步hello world
abs(-565)
#这是python中求一个数绝对值的函数
#这一行为什么没有在屏幕上出现？
print abs(-565) 
#如果没有print语句则abs函数并不能在屏幕中输出-565的绝对值
#除了上述方法我们还可以用下面的方法输出Hello world!
wordstring='hello world!'
#首先我们定义了一个变量wordstring，将所要输出的hello world!赋给变量wordstring
print wordstring
#使用print语句将变量wordstring中的hello world!输出
#那么如果我们不用print语句将出现什么效果？
#wordstring
#在我使用的python 2.7.10中无法显示变量的内容？
print "this is my first python program ! %s"%(wordstring)
#在python中我们也可以用%s这种，我们将已经定义好的wordstring传入%s中，这和c中的printf很像
#既然有了输出我们就学习一下输入
myname = raw_input('please input your name :')
#这条语句中有python中标准输入，它将我们在键盘上输入的数据传给我们在语句中定义的myname
print "my name is %s"%(myname)
#我们再利用前面学到的print语句将myname中的数据打印在屏幕上


