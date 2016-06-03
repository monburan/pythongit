import time
#print time.localtime()
def pro_time():
    print 'start!'
    time.sleep(2)

t0 = time.clock()
pro_time()
print time.localtime(),t0
t1 = time.clock()
print time.localtime(),t1
if (t1-t0):
    print 'too late'
