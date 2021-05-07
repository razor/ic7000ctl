#!/usr/bin/env python

import socket, struct
from wsjtx_decoder import *
from rigctl import *

logging.Logger.setLevel(logging.getLogger(), logging.INFO)

localIP = "127.0.0.1"
localPort =  2237
bufferSize = 1024

rigctl = RigCtl()

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    wsjtxmsg = WSJTX_Packet(message, 0)
    wsjtxmsg.Decode()
    
    if wsjtxmsg.PacketType == 0:
    # heartbeat
        pass
    elif wsjtxmsg.PacketType == 1:
    # status
        statusmsg = WSJTX_Status(message, wsjtxmsg.index)
        statusmsg.Decode()
        rigctl.setFreq(statusmsg.Frequency)
    elif wsjtxmsg.PacketType == 2:
    # decodes
        pass
    elif wsjtxmsg.PacketType == 6:
    # close
    #    rigctl.close()
    #    break
        pass
