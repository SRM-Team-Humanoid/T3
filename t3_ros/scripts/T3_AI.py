#!/usr/bin/env python
# Tic Tac Toe v3. Start as Both Player. ROS Integrated :)
from copy import deepcopy
import rospy
from std_msgs.msg import String

def charval(a):
    global splayer
    if a == 0:
        return ('_')
    if a == 3 and splayer == 1:
        return ('O')
    if a == 5 and splayer == 1:
        return ('X')
    if a == 3 and splayer == -1:
        return ('X')
    if a == 5 and splayer == -1:
        return ('O')


def disp(board):
    print
    print
    for i in range(3):
        for j in range(3):
            print(charval(board[i][j])),
        print
    print


def terminal(board):
    if board[0][0] + board[0][1] + board[0][2] == 9:
        return 1
    if board[1][0] + board[1][1] + board[1][2] == 9:
        return 1
    if board[2][0] + board[2][1] + board[2][2] == 9:
        return 1
    if board[0][0] + board[1][0] + board[2][0] == 9:
        return 1
    if board[0][1] + board[1][1] + board[2][1] == 9:
        return 1
    if board[0][2] + board[1][2] + board[2][2] == 9:
        return 1
    if board[0][0] + board[1][1] + board[2][2] == 9:
        return 1
    if board[0][2] + board[1][1] + board[2][0] == 9:
        return 1

    if board[0][0] + board[0][1] + board[0][2] == 15:
        return 2
    if board[1][0] + board[1][1] + board[1][2] == 15:
        return 2
    if board[2][0] + board[2][1] + board[2][2] == 15:
        return 2
    if board[0][0] + board[1][0] + board[2][0] == 15:
        return 2
    if board[0][1] + board[1][1] + board[2][1] == 15:
        return 2
    if board[0][2] + board[1][2] + board[2][2] == 15:
        return 2
    if board[0][0] + board[1][1] + board[2][2] == 15:
        return 2
    if board[0][2] + board[1][1] + board[2][0] == 15:
        return 2
    if (0 in board[0] or 0 in board[1] or 0 in board[2]):
        return 0
    else:
        return -1


def getinput():
    x = int(raw_input()) - 1
    while (x not in range(9)):
        x = int(raw_input()) - 1
    return x


def update(board, player, x):
    new_board = deepcopy(board)
    if player == 1:
        if new_board[x / 3][x % 3] == 0:
            new_board[x / 3][x % 3] = 3
    if player == -1:
        if new_board[x / 3][x % 3] == 0:
            new_board[x / 3][x % 3] = 5

    return new_board


def utility(board):
    global splayer
    if terminal(board) == -1:
        return 0
    if terminal(board) == 1:
        return 1 * player
    if terminal(board) == 2:
        return -1 * player


def actions(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                moves.append(3 * i + j)
    return moves


count = 0


def minimax(depth, board, maxplayer):
    if depth == 0 or terminal(board) != 0:
        return utility(board)

    if maxplayer:
        val = -2
        for move in actions(board):
            val2 = minimax(depth - 1, update(board, 1, move), False)
            val = max(val, val2)
        return val
    else:
        val = 2
        for move in actions(board):
            val2 = minimax(depth - 1, update(board, -1, move), True)
            val = min(val, val2)
        return val


def getminmax(board):
    count = 0
    move = 599
    val = -2
    lista = []
    for action in actions(board):
        print(actions(board).index(action))
        x = minimax(9, update(board, 1, action), False)
        lista.append(x)
        if x > val:
            val = x
            move = action
    return move

#--------------------------------------------------------------------------------------------


read = False
input = 0
start = 0
if_reset = 0



def reader(data):
    global read,input,start,if_reset
    try:
        print "Bhai Mera Swag"
        input = int(data.data)
        print input
        read = True
    except:
        read=True
        print "get"
        start = data.data[0]
        if start == 'o':
            if_reset=1
            start = 1
        else:
            if_reset=2
            start = 2




def reset(choice):
    global splayer,player,board,init,read
    board = [[0 for x in range(3)] for x in range(3)]

    print("Select Option - ")
    print("1)Start First")
    print("2)Start Second")
    init = True
    read = False
    if choice==2:
        splayer = 1
        player = 1
    elif choice ==1:
        splayer = -1
        player = -1
    else:
        print "Invalid"
        exit()



rospy.init_node('AI')
rospy.Subscriber('input',String,reader)
writer = rospy.Publisher('output', String, queue_size=1)



board = [[0 for x in range(3)] for x in range(3)]

print("Select Option - ")
print("1)Start First")
print("2)Start Second")

while start==0:
    pass
choice = start
init = True
if choice == 2:
    splayer = 1
    player = 1
elif choice == 1:
    splayer = -1
    player = -1
else:
    print "Invalid"
    exit()

print "done1"
read = False
if_reset = 0



while (True):
    print "done2"
    if if_reset>0:
        reset(if_reset)
        if_reset=0
    disp(board)
    print "done3"
    if player == 1:
        print "done4"
        if init:
            x = 0
        else:
            x = getminmax(board)
        writer.publish(str(x+1))
        print "done5"
    elif player == -1:
        print "done6"
        while not read:
            pass
        x = input - 1
        read = False
        if x not in actions(board):
            print ("Invalid Move. Try Again")
            continue
        print "done7"
    board = update(board, player, x)
    player *= -1
    init = False
    if (terminal(board) != 0):
        disp(board)
        if (utility(board) == -1):
            print "Computer Wins!"
            writer.publish("win")
        if (utility(board) == 1):
            print "You Win!"
        if (utility(board) == 0):
            print "Draw"
            writer.publish("win")
        while if_reset==0:
            pass
rospy.spin()





















































