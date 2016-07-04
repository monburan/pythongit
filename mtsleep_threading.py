import threading
from time import ctime,sleep

loops = [4,2]
def loop(nloop,nsec):
    print 'start loop',nloop,'at:',ctime()
    sleep(nsec)
    print 'stop loop',nloop,'at:',ctime()

def main():
    print 'start program at:',ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target = loop,args = (i,loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()
    
    for i in nloops:
        threads[i].join()

    print 'stop program at:',ctime()

if __name__ == '__main__':
    main()
