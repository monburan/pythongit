import thread
from time import sleep,ctime

loops = [4,2,5,1]
def loopdef(nloop,nsec,lock):
    print nloop," start time ",ctime()
    sleep(nsec)
    print nloop," stop time",ctime()
    lock.release()

def main():
    print "program start time ",ctime()
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loopdef,(i,loops[i],locks[i]))
    for i in nloops:
        while locks[i].locked():pass
    print "program stop time ",ctime()
if __name__ == "__main__":
    main()
