#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
TCP_IP = '192.168.1.2' # Get local machine name
port = 7003                # Reserve a port for your service.

s.connect((TCP_IP, port))
s.send('9')
s.close                                                                                                                                                                                                                          
