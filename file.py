#coding:UTF-8
filename = raw_input('Enter file name:')
#fileobj = open(filename,'r')
#for eachline in fileobj:
#    print eachline,
#fileobj.close()
#filewriteobj = open(filename,'w')
#��������ͨ��wģʽ�����ļ�
#filewriteobj.write("writing in this txt file!")
#����֮����ֱ��ʹ��readline���ļ���
#���ֱ��ʹ��readline�����ᱨ��IOError: File not open for reading
#filewriteobj.close()
#filereadobj = open(filename,'r')
#�������ǽ��ļ�ͨ��rģʽ�򿪣��Ϳ��Խ�����֮ǰд�õ������ʾ����Ļ����
#print filereadobj.readline()
#д���쳣�׳�����һ�¾ٵ�����
#try:
#    fobj = open(filename,'w')
#    fobj.write("writing in this txt file!")
#    print fobj.readline()
#except IOError,e:
#    print 'file error is :',e
#���н��file error is : File not open for reading
fileobj = open(filename,'w')
fileobj.write("writing in this txt file!")
fileobj.close()
fileobj = open(filename,'r')
print fileobj.readline()
