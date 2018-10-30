import socket

# Just a sample program to open a socket to read data from an IP
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.connect(("google.com",80))
# s.send(b"GET /index.html HTTP/1.0\n\n")
# data = s.recv(10000) # No of bytes to receive
# print(data)
# s.close()


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("",9002))
s.listen(5)
#s.settimeout(10)
while True:
    c, a = s.accept()
    try:
        while True:
            data = c.recv(100000)
            if data:
                data = str(data,'utf-8').upper()
                print("Data send is", data.upper())
                c.sendall(bytes(data,'utf-8'))
            else:
                print("No data")
                break
    finally:
        c.close()

# UDP server
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(("",9002))
# while True:
#     data, addr = s.recvfrom(20)
#     resp = str(data,'utf-8').upper()
#     s.sendto(bytes(resp,'utf-8'),addr)

