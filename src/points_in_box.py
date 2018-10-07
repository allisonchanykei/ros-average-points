#!/usr/bin/env python

import rospy
from avg_points.msg import Point, BoundingBox


class Box:
    def __init__(self):
        self.numPoints = 0
        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0

    def addToBox(self, point):
        if point.x <= self.right and point.x >= self.left and point.y >= self.bottom and point.y <= self.top:
            self.numPoints += 1

    def updateBox(self, box):
        if box:
            self.numPoints = 0
            self.left = box.points[0].x
            self.right = box.points[1].x
            self.top = box.points[0].y
            self.bottom = box.points[1].y
            if box.points[0].x > box.points[1].x:
                self.left = box.points[1].x
                self.right = box.points[0].x
            if box.points[0].y < box.points[1].y:
                self.top = box.points[1].y
                self.bottom = box.points[0].y

    def stringify(self):
        return "top: %2f, bottom: %2f, left: %2f, right: %2f" % (self.top, self.bottom, self.left, self.right)


def callbackPoint(data, box):
    box.addToBox(data)


def callbackBox(data, box):
    rospy.loginfo('Number of Points in box: %d', box.numPoints)
    box.updateBox(data)
    rospy.loginfo(box.stringify())


def listener():
    box = Box()

    rospy.init_node('points_in_box', anonymous=True)
    rospy.Subscriber('random_point', Point, callbackPoint, box)
    rospy.Subscriber('random_box', BoundingBox, callbackBox, box)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
