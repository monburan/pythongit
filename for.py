#coding:UTF-8
#print "i'd like to use the internet for:"
#for item in ['surfing internnet','chat with my friend','learn more python']:
#    print item
#两种不同的用法
#print "i'd like to use the internet for:"
#for item in ['surfing internnet','chat with my friend','learn more python']:
#    print item,
#    print
#最后一句句尾的","可以改变print语句默认的自动换行
#for ABC in ["A","B","C"]:
#    print ABC
#for number in range(5):
#    print number

#mystring = 'this is a string'
#for f in mystring:
#    print f,
#for i in range(len(mystring)):
#    print mystring[i],"%d"%(i)

#squared = [x**2 for x in range(4)]
findx2 = [x**2 for x in range(8) if not x % 2]
for i in findx2:
    print i