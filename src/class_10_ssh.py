import paramiko
import sys

# Program to connect through SSH to a remote server
import os
def printTotal(trans,tobetransfer):
    print("Transfereed data ", trans,tobetransfer)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='localhost',username='cisco',password='cisco',port='22')
sftp = ssh.open_sftp()
localpath = 'class_9_pdb.py'
remotepath = '/tmp/myname.py'
sftp.put(localpath,remotepath,callback=printTotal)
sftp.close()
ssh.close()

# Program to send large data with progress bar
# from tqdm import tqdm # module of progress bar
#
# def viewBar(a,b):
#     res = a/int(b) * 100
#     sys.stdout.write("\rComplete percent: %0.2f "% res)
#     #sys.stdout.flush()
#
# def viewBar2(a,b):
#     #print(a,b)
#     pbar = tqdm(total=int(b),ascii=False,unit='b',unit_scale=True)
#     pbar.update(a)
#
# t = paramiko.Transport(('localhost',22))
# t.connect(username='cisco',password='cisco')
#
# sftp = paramiko.SFTPClient.from_transport(t)
# sftp.put("/home/cisco/Python-3.5.5.tgz",'/tmp/myfile.tgz',callback=viewBar2)
# t.close()

# Program to connect to ftp server
# import ftplib
# f = ftplib.FTP("ftp.gnu.org","anonymous",'mymail@domain.com')
# files = []
# f.retrlines("NLST",files.append)

# Program to connect to a server through HTTP connection
# import httplib2
# c= httplib2.HTTPConnectionWithTimeout("www.gnu.org")
# c.putrequest("GET","/philosophy/philosophy.html")
# c.putheader("Someheader","SomeValue")
# c.endheaders()
#
# r = c.getresponse()
# data = r.read()
# print(str(data,'utf-8'))
# c.close()

from BasicHttpServer import CGIHTTPRequestHandler,HTTPServer

# class HelloHandler(CGIHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == "/hello":
#             self.send_response(200,"OK")
#             self.send_header("Content-type","text/HTML")
#             self.end_headers()
#             self.wfile.write(b"""<HTML>
#             <HEAD><TITLE>Hello</TITLE>
#             <BODY>Hello world...</BODY></HEAD></HTML>""")
# serv = HTTPServer(("",8081),HelloHandler)
# serv.serve_forever()