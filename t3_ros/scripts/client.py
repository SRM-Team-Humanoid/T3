#!/usr/bin/env python

import socket               # Import socket module
import netifaces as ni

s = socket.socket()         # Create a socket object
TCP_IP = ni.ifaddresses('wlan0')[2][0]['addr'] # Get local machine name
port = 7003                # Reserve a port for your service.

s.connect((TCP_IP, port))
s.send('9')
s.close
