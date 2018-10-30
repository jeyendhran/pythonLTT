import ftplib
import paramiko
import re
import socket
import logging

WEBSITE = "ftp.gnu.org"
LOCAL_FILE_NAME = "readme.txt"

LOG_FILENAME = 'logging_example.out'

logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)


def LoggingDecorator(func):
    def decorator(*args,**kwargs):
        logging.debug(func.__doc__)
        ret = func(*args,**kwargs)
        return ret
    return decorator

@LoggingDecorator
def readUrlFiles(url):
    '''********Fetching files from URL***********'''
    f = ftplib.FTP(url,"anonymous",'mymail@domain.com')
    files = []
    f.retrlines("NLST",files.append)
    return files

@LoggingDecorator
def findFile(filename,pattern):
    '''***********Find matched files*************'''
    readme_file = ""
    for file in filename.split(","):
        file_name = pattern.search(file)
        if file_name is not None:
            readme_file = file_name.group(0)
            break
    else:
        print("File not found")
    return readme_file

@LoggingDecorator
def readData(filename,url):
    """**********Reading README data***********"""
    ftp = ftplib.FTP(url, 'anonymous', 'bwdayley@novell.com')
    fp = open(LOCAL_FILE_NAME, "wb")
    fileurl = 'RETR ' + filename
    ftp.retrbinary(fileurl, fp.write)
    fp.close()
    ftp.quit()

    fp = open(LOCAL_FILE_NAME, "r")
    data = fp.read()
    fp.close()
    return data

@LoggingDecorator
def findMatchedLine(pattern,data):
    """*********Finding 'the' matched lines*********"""
    matched_lines = []
    for line in data.split("\n"):
        matched_line = pattern.search(line)
        if matched_line:
            matched_lines.append(line)
    return matched_lines

@LoggingDecorator
def getUpperCased(matched_lines):
    """**************Upper cased the readed lines*************"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9002)
    sock.connect(server_address)
    uppercased_lines = []
    try:
        for line in matched_lines:
            message = bytes(line,'utf-8')
            sock.sendall(message)

            amount_received = 0
            amount_expected = len(message)
            data = b""
            data = sock.recv(len(message))
            uppercased_lines.append(str(data,"utf-8"))
    finally:
        sock.close()
    return uppercased_lines

@LoggingDecorator
def writeLines(data,filename):
    """*******Writing data to a file*************"""
    f = open(filename,"w")
    f.write("\n".join(data))
    f.close()
    return True

@LoggingDecorator
def sendFiles(filename):
    """***********Sending data to FTP server************"""
    def printTotal(trans,tobetransfer):
        print("Transfereed data ", trans,tobetransfer)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='localhost',username='cisco',password='cisco',port='22')
    sftp = ssh.open_sftp()
    localpath = filename
    remotepath = "/tmp/myfile.txt"
    sftp.put(localpath,remotepath,callback=printTotal)
    sftp.close()
    ssh.close()

@LoggingDecorator
def endfun():
    """End of process"""
    pass

if __name__ == '__main__':
    serverfiles = readUrlFiles(WEBSITE)
    print(serverfiles)
    readme_pattern = re.compile("^README$")
    readme_file = findFile(",".join(serverfiles),readme_pattern)

    readme_data = readData(str(readme_file),WEBSITE)

    the_pattern = re.compile("the")
    matched_lines = findMatchedLine(the_pattern,readme_data)
    newlines = getUpperCased(matched_lines)
    print(newlines)
    if writeLines(newlines,LOCAL_FILE_NAME):
        sendFiles(LOCAL_FILE_NAME)
    endfun()