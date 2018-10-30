import threading
import time

x = 0

def inc_x(inc):
    global x
    x = x + inc
    print("Inc_x",x)

def print_x(val):
    global x
    print("The value is",(x+val))

def myfun(string,sleeptime,lock):
    while True:
        # entering into critical section
        lock.acquire()
        print(string, "sleeping for",sleeptime,"seconds")
        time.sleep(sleeptime)
        print(string,"Releasing")
        lock.release()
        # exiting from critical section
        #time.sleep(sleeptime) # to sleep current thread so that next thread will execute in the mean time

#
# lock = _thread.allocate_lock()
#
# _thread.start_new_thread(myfun,("Thread:1",2,lock))
# _thread.start_new_thread(myfun, ("Thread:2", 2, lock))
# _thread.start_new_thread(inc_x,(5,))
# _thread.start_new_thread(print_x,(2,))

# class PrintTime(threading.Thread):
#     def __init__(self,name,interval):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.interval = interval
#     def run(self):
#         while True:
#             time.sleep(self.interval)
#             print("Thread name", self.name)
#             print("Time is",time.ctime())
#
# p1 = PrintTime("Thread1",2)
# p1.start()
# p2 = PrintTime("Thread2",3)
# p2.start()

def loop(nloop,sec):
    print(nloop,"going to sleep for",sec,"seconds")
    time.sleep(sec)
    print(nloop, "come out of sleep")

loops = [2,2]
nloops = range(len(loops))
threads = []
for i in nloops:
    t = threading.Thread(target=loop,args=(i,loops[i]))
    threads.append(t)

for i in nloops:
    threads[i].start()

for i in nloops:
    threads[i].join()

while True:
    pass