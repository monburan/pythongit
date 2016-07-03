import thread
from time import sleep,ctime

def loop0():
    print "loop0 start time ",ctime()
    sleep(3)
    print "loop0 stop time",ctime()

def loop1():
    print "loop1 start time ",ctime()
    sleep(2)
    print "loop1 stop time",ctime()

def main():
    print "program start time ",ctime()
    thread.start_new_thread(loop0,())
    thread.start_new_thread(loop1,())
    sleep(6)
    print "program stop time ",ctime()
if __name__ == "__main__":
    main()
