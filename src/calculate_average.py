#!/usr/bin/env python

import rospy
from avg_points.msg import Point

# def talker():


def callback(data):
    callback.sumx += data.x
    callback.sumy += data.y
    callback.n += 1
    rospy.loginfo('n: %d', callback.n)
    rospy.loginfo('x: %2f, y: %2f', callback.sumx/callback.n, callback.sumy/callback.n)


def listener():
    callback.sumx = callback.sumy = callback.n = 0

    rospy.init_node('average_calculator', anonymous=True)
    rospy.Subscriber('random_point', Point, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
