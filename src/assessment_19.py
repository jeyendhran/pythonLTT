import os
import paramiko

def getLargestfile(path):
    files = os.listdir(path)
    file_info = dict(zip([x for x in files],[os.stat(file).st_size for file in files]))
    file_size = list(file_info.values())
    for name,size in file_info.items():
        if size == max(file_size):
            filename = name
    print("The size of largest file is", max(file_size), "bytes and the name of the file is",filename)
    return filename

def filestatus(trans,tobetransfer):
    print("Transfereed data ", trans,tobetransfer)

def sendFile(filename):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='localhost', username='cisco', password='cisco', port='22')
    sftp = ssh.open_sftp()
    localpath = filename
    remotepath = '/tmp/'+filename
    sftp.put(localpath, remotepath,callback=filestatus)
    sftp.close()
    ssh.close()

def sendfile2(filename):
    t = paramiko.Transport(('localhost', 22))
    t.connect(username='cisco',password='cisco')

    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(filename,'/tmp/'+filename,callback=filestatus)
    t.close()

filename = getLargestfile(".")
sendfile2(filename)