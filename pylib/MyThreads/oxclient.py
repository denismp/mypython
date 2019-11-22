'''
Created on Mar 30, 2011

@author: putnam
'''

# Echo client program
import socket

filler = ""

fileName = "filler.txt"

try:
    FH = open(fileName, "r")
    filler = FH.read()
    FH.close()
except IOError as inst:
    raise
# Endtry

# HOST = 'freedom.dynalias.org'    # The remote host
HOST = 'localhost'  # The remote host
PORT = 50007  # The same port as used by the server

for i in range(5):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # msgNum = socket.htonl(i)
    # msgNum = socket.htonl(int( str( i ),16))
    # print 'msgNum=', msgNum

    # myHex = "%-04.4x" % ( int( str( i ), 16 ) )
    # socket.htonl(x)

    msgNum2 = socket.htonl(int(str(i)))
    print('msgNum2=', msgNum2)

    # socket.ntohl(x)
    # msgNum3 = socket.ntohl(long( msgNum2 ))
    # print 'msgNum3=', msgNum3

    # print 'myHex=', myHex

    s.send(str(msgNum2).encode())
    s.send(filler.encode())
    data = s.recv(2048)
    s.close()
    print('Received', repr(data))
