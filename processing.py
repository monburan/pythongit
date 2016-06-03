import multiprocessing
import time
import random
def worker():
    n = random.random()
    while n > 0:
        print "Time is " + time.ctime()
        time.sleep(2)
        n -= 1
if __name__ == "__main__":
    p1 = multiprocessing.Process(target = worker)
    p2 = multiprocessing.Process(target = worker)
    p3 = multiprocessing.Process(target = worker)
    p4 = multiprocessing.Process(target = worker)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    
    print "CPU Numbers:"+str(multiprocessing.cpu_count())

    print "p.pid:",p1.pid
    print "p.name:"+p1.name
    print "p.is_alive:",p1.is_alive()
    print "p.pid:",p2.pid
    print "p.name:"+p2.name
    print "p.is_alive:",p2.is_alive()
    print "p.pid:",p3.pid
    print "p.name:"+p3.name
    print "p.is_alive:",p3.is_alive()
    print "p.pid:",p4.pid
    print "p.name:"+p4.name
    print "p.is_alive:",p4.is_alive()
