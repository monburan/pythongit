#coding:UTF-8
from random import choice

def erfen(a,b,n):
    while a<b:
        mid = (a+b)/2
        if n == mid:
            print "上界a:%d,下界b:%d,中间值:%d,随机数:%d"%(a,b,mid,n)
            return n
        if n < mid:
            print "上界a:%d,下界b:%d,中间值:%d,随机数:%d"%(a,b,mid,n)
            b = mid - 1
        if n > mid:
            print "上界a:%d,下界b:%d,中间值:%d,随机数:%d"%(a,b,mid,n)
            a = mid + 1
def main():
    a = int(raw_input("请输入数字a作为上界:"))
    b = int(raw_input("请输入数字b作为下界:"))
    n = choice(range(a,b))
    mid = erfen(a,b,n)
    print mid
if __name__ == "__main__":
    main()
