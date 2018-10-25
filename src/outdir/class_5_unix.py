def write_file(val):
    f = open("osfile.txt",'w')
    f.write("x = "+str(val))
    f.close()

def read_file():
    f = open("osfile.txt")
    print("contents of file",f.read())
    f.close()

import os
write_file(10)
pid = os.fork()
print(pid)

if pid == 0:
    print("PPID is",os.getppid())
    print("Hello world from child",os.getpid())
    read_file()
    write_file(11)
else:
    os.wait()
    print("Hello world from parent",os.getpid())
    read_file()
