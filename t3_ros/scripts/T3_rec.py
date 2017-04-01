#!/usr/bin/env python

import rospy
from std_msgs.msg import String


board = ['_','_','_','_','_','_','_','_','_']


def disp(board):
    for i in range(3):
        print board[i],
    print
    for i in range(3,6):
        print board[i],
    print
    for i in range(6,9):
        print board[i],
    print


def update(data):
    global board
    str = data.data
    num = int(str[0])
    num -= 1
    board[num]=str[1]
    disp(board)
    print
    print




if __name__ == '__main__':
    rospy.init_node('display', anonymous=True)
    rospy.Subscriber('output', String, update)
    rospy.spin()
