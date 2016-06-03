#coding:UTF-8
filename = raw_input('Enter file name:')
#fileobj = open(filename,'r')
#for eachline in fileobj:
#    print eachline,
#fileobj.close()
#filewriteobj = open(filename,'w')
#这里我们通过w模式将打开文件
#filewriteobj.write("writing in this txt file!")
#在这之后不能直接使用readline将文件打开
#如果直接使用readline语句则会报错IOError: File not open for reading
#filewriteobj.close()
#filereadobj = open(filename,'r')
#这是我们将文件通过r模式打开，就可以将我们之前写好的语句显示在屏幕上了
#print filereadobj.readline()
#写个异常抛出来看一下举得例子
#try:
#    fobj = open(filename,'w')
#    fobj.write("writing in this txt file!")
#    print fobj.readline()
#except IOError,e:
#    print 'file error is :',e
#运行结果file error is : File not open for reading
fileobj = open(filename,'w')
fileobj.write("writing in this txt file!")
fileobj.close()
fileobj = open(filename,'r')
print fileobj.readline()
