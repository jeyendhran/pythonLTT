import os
import time
import signal
# pid = os.fork()
# x = 10
#
# if pid == 0:
#     time.sleep(5)
#     #os.execlp("ls", "ls")
#     #os.execl("/bin/ls","/bin/ls")
#     print("PPID is", os.getppid())
#     print("Hello world from child", os.getpid())
#     x = 11
# else:
#     #os.wait()
#     print("Hello world from parent", os.getpid())
#     print(x)

# def sighandler(a,b):
#     print("From my handler",a,"b value is",b)
#     #os.sys.exit()
#     signal.signal(signal.SIGINT,signal.SIG_DFL)
#
# signal.signal(signal.SIGINT, sighandler)
#
# while True:
#     print("Hi All")
#     time.sleep(1)

# def alarm_handler(a,b):
#     print("I am alarm",time.ctime(),a,b)
#
# signal.signal(signal.SIGALRM, alarm_handler)
# signal.alarm(4)
# print("Time is",time.ctime())
# time.sleep(5)

fd = os.open("output.txt",os.O_CREAT|os.O_WRONLY, 644)
os.write(fd,b"Hellooooo")
print(fd)
os.close(fd)

fd = os.open("output.txt",os.O_RDONLY)
cnt = 1
while cnt:
    cnt = os.read(fd,1)
    os.write(1,cnt)
    #print(str(cnt))
os.close(fd)

class Myclass:
    def __init__(self):
        self.name = "Jeyendhran"

import pickle
f = open("student.bin","wb")
me = Myclass()
pickle.dump(me,f)
f = open("student.bin","rb")
s = pickle.load(f)
print(s )