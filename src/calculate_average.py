#!/usr/bin/env python

import rospy
from avg_points.msg import Point

#def talker():

def callback(data):
    rospy.loginfo('x: %2f, y: %2f', data.x, data.y)

def listener():
    rospy.init_node('average_calculator', anonymous=True)
    rospy.Subscriber('random_point', Point, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
