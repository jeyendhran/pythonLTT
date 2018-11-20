import socket
import pickle

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("",9002))
s.listen(5)
s.settimeout(10)
while True:
    c, a = s.accept()
    try:
        while True:
            data = c.recv(100000)
            if data:
                message = pickle.loads(data)
                message.name = message.name.upper()
                message = pickle.dumps(message)
                c.sendall(message)
            else:
                print("No data")
                break
    finally:
        c.close()
