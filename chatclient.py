# -*- coding:utf-8 -*-
# !/usr/bin/env python

# telnet program example
import socket, select, string, sys

from cryptocesear import checkKeys, decryptMessage, encryptMessage, getKeyParts, getRandomKey, SYMBOLS


# myKey = raw_input('Entrer la clé de cryptage : ')
# myKey = int(myKey)

def prompt():
    # sys.stdout.read()
    sys.stdout.flush()
    sys.stdout.write('YOU : ')


myKey = raw_input('Entrer la clé de cryptage : ')
myKey = int(myKey)

# main function
if __name__ == "__main__":

    if len(sys.argv) < 3:
        print 'Usage : python telnet.py hostname port'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # connect to remote host
    try:
        s.connect((host, port))
    except:
        print 'Unable to connect'
        sys.exit()

    print 'Connected to remote host. Start sending messages'
    prompt()

    while 1:
        socket_list = [sys.stdin, s]

        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

        for sock in read_sockets:
            # incoming message from remote server
            if sock == s:
                data = sock.recv(4096)
                if not data:
                    print '\nDisconnected from chat server'
                    sys.exit()
                else:
                    # print data
                    print '\nData value0:'+data
                    data = decryptMessage(myKey, data)
                    print '\nData Value2' + data
                    sys.stdout.write(data)
                    prompt()

            # user entered a message
            else:

                msg = sys.stdin.readline()
                print '\nMessage value0:' + msg
                msg = encryptMessage(myKey, msg)
                print '\nMessage value0:' + msg
                s.send(msg)
                prompt()
