#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def proc():
    return raw_input(">>")



def pub_input():
    pub = rospy.Publisher('input', String, queue_size=1)
    rospy.init_node('input', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = proc()
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        pub_input()
    except rospy.ROSInterruptException:
        pass
