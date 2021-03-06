#!/usr/bin/env python

import rospy
from avg_points.msg import Point
from random import uniform


def generate_number():
    return uniform(-100, 100)


def generate_point():
    point = Point()
    point.x = generate_number()
    point.y = generate_number()
    return point


def talker():
    pub = rospy.Publisher('random_point', Point, queue_size=10)
    rospy.init_node('point_generator', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        point = generate_point()
        rospy.loginfo('x: %2f, y: %2f', point.x, point.y)
        pub.publish(point)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
