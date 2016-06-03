#coding:UTF-8
def fun1(x):
    return x+x
#def是python中函数的关键字，fun是命名的函数名,()中是函数参数
#函数写好了，可以用下面的方法实现它
x = raw_input('please input something:')
print fun1(x)
#在函数中可以存在一个默认值，函数在调用的时候如果没有传入参数，函数就会自动调用这个值做默认值
def fun2(x=1):
    if x==1:
        print "this is one"
    else:
        print "noop"
fun2(1)
fun2(2)