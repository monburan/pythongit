#coding:UTF-8
def fun1(x):
    return x+x
#def��python�к����Ĺؼ��֣�fun�������ĺ�����,()���Ǻ�������
#����д���ˣ�����������ķ���ʵ����
x = raw_input('please input something:')
print fun1(x)
#�ں����п��Դ���һ��Ĭ��ֵ�������ڵ��õ�ʱ�����û�д�������������ͻ��Զ��������ֵ��Ĭ��ֵ
def fun2(x=1):
    if x==1:
        print "this is one"
    else:
        print "noop"
fun2(1)
fun2(2)