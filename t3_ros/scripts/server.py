#!/usr/bin/env python
import socket
import rospy
from std_msgs.msg import String
import netifaces as ni


mapper = {1:3,2:6,3:9,4:2,5:5,6:8,7:1,8:4,9:7}
re_mapper = {3:1,6:2,9:3,2:4,5:5,8:6,1:7,4:8,7:9}

if __name__ == '__main__':
    pub = rospy.Publisher('input', String, queue_size=10)
    rospy.init_node('input_pub', anonymous=True)
    try:
        prev = 0
        s = socket.socket()         # Create a socket object
        done_indices = []
        TCP_IP = ni.ifaddresses('wlan0')[2][0]['addr'] # Get local machine name
        port = 7004    # Reserve a port for your service.
        s.bind((TCP_IP, port))        # Bind to the port
        s.listen(5)                 # Now wait for client connection.
        c, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr
        while True:
            m= c.recv(16)
            print m

            if m[1]=='0':
                pub.publish(m)
                done_indices = []
                continue

            if m[0]!='o':
                continue
            m = m[1]
            m = re_mapper[int(m)]
            m = str(m)
            if m!= "" and m not in done_indices:
                done_indices.append(m)
                rospy.loginfo(m)
                pub.publish(m)
            # else :
            #     print "error"
            #     c.close()
            #     break
    except rospy.ROSInterruptException:
        pass
