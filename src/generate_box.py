#!/usr/bin/env python

import rospy
from avg_points.msg import Point, BoundingBox
from generate_points import generate_point


def generate_box():
    box = BoundingBox()
    for i in range(2):
            box.points[i] = generate_point()
    return box


def talker():
    pub = rospy.Publisher('random_box', BoundingBox, queue_size=10)
    rospy.init_node('box_generator', anonymous=True)
    rate = rospy.Rate(0.1)  # every 10s
    while not rospy.is_shutdown():
        box = generate_box()
        rospy.loginfo(str(box.points))
        pub.publish(box)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
