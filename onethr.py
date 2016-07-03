from time import sleep,ctime

def loop0():
    print "loop0 start time ",ctime()
    sleep(3)
    print "loop0 stop time",ctime()

def loop1():
    print "loop1 start time ",ctime()
    sleep(1)
    print "loop1 stop time  ",ctime()

if __name__ == "__main__":
    print "program start time ",ctime()
    loop0()
    loop1()
    print "program stop time ",ctime()

