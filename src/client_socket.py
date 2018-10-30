import socket

# Create a TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # Connect the socket to the port where the server is listening
# server_address = ('localhost', 9002)
# print('connecting to {} port {}'.format(*server_address))
# sock.connect(server_address)
#
# try:
#
#     # Send data
#     message = b'This is the message.  It will be repeated.'
#     print('sending {!r}'.format(message))
#     sock.sendall(message)
#
#     # Look for the response
#     amount_received = 0
#     amount_expected = len(message)
#
#     while amount_received < amount_expected:
#         data = sock.recv(20)
#         amount_received += len(data)
#         print('received ',str(data,'utf-8'))
#
# finally:
#     sock.close()

#UDP client
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sent = s.sendto(b"This is the message", ("",9002))
try:
    # Receive response
    print('waiting to receive')
    data, server = s.recvfrom(20)
    print('received {!r}'.format(data))
finally:
    s.close()