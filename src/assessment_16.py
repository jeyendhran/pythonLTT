import os
import subprocess

pid = os.fork()
empty_files = []
if pid == 0:
    files = os.listdir(".")
    empty_files = list(filter(lambda x: os.stat(x).st_size == 0,files))

    # for file in files:
    #     if os.stat(file).st_size == 0:
    #         empty_files.append(file)

    with open("empty_files.txt","w") as f:
        f.write(",".join(empty_files))
else:
    os.wait()
    if os.stat("empty_files.txt").st_size == 0:
        print("Empty file deleted")
        os.unlink("empty_files.txt")
    else:
        with open("empty_files.txt","r") as f:
            empty_files = f.read().split(",")
        print("Empty files are",empty_files)
        if len(empty_files)>1:
            [os.unlink(x) for x in empty_files]
