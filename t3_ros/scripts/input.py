#!/usr/bin/env python

import socket
import netifaces as ni

s = socket.socket()
TCP_IP=ni.ifaddresses('wlan0')[2][0]['addr']
port = 7003

s.connect((TCP_IP,port))
s.send('9')
s.close()
