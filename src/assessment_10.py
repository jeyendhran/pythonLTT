import socket
import pickle
import doctest
import unittest

from Student import *

class Myrun(unittest.TestCase):
    def testcasing(self):
        self.assertTrue(getData() .isupper() == True)

def getName(name):
    '''
    #     >>> getName('jeyendhran')
    #     False
    #     >>> getName('NAME')
    #     True
    #     '''
    return name.isupper()


def getData():
    username = ""
    s = Student("Jeyendhran", 23)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 9002)
    sock.connect(server_address)

    try:
        # Send data
        print("The name in sent obj is", s.name)
        message = pickle.dumps(s)
        # print('sending {!r}'.format(message))
        sock.sendall(message)

        # Look for the response
        data = sock.recv(100000)
        data = pickle.loads(data)
        username = data.name

        print("The name in received obj is", data.name)

    finally:
        sock.close()
    return username

if __name__ == '__main__':
    # print(getData())

    # suite = unittest.TestLoader().loadTestsFromTestCase(Myrun)
    # unittest.TextTestRunner(verbosity=1).run(suite)

    # doctest.testmod(verbose=True)
    # print(getName('sif'))
    # print(getName('JEY'))
