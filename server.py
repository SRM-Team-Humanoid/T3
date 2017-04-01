#!/usr/bin/env python
import socket
import rospy
from std_msgs.msg import String


if __name__ == '__main__':
    pub = rospy.Publisher('input', String, queue_size=10)
    rospy.init_node('input_pub', anonymous=True)
    try:
        prev = 0
        s = socket.socket()         # Create a socket object
        done_indices = []
        TCP_IP = '192.168.1.7' # Get local machine name
        port = 7003      # Reserve a port for your service.
        s.bind((TCP_IP, port))        # Bind to the port
        s.listen(5)                 # Now wait for client connection.
        c, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr
        while True:
            m= c.recv(16)
            if m!= "" and m not in done_indices:
                done_indices.append(m)
                rospy.loginfo(m)
                pub.publish(m)
            else :
                print "error"
                c.close()
                break
    except rospy.ROSInterruptException:
        pass
