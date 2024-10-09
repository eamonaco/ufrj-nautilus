#!/usr/bin/python3

import rospy
from geometry_msgs.msg import PoseStamped


rospy.init_node('sun_position')

pub = rospy.Publisher('/sun_pose', PoseStamped, queue_size=10)


while not rospy.is_shutdown():
    pos = PoseStamped()

    pos.header.stamp = rospy.Time.now()
    pos.header.frame_id = 'sun'

    pos.pose.position.x = 2
    pos.pose.position.y = 1
    pos.pose.position.z = 0

    pos.pose.orientation.x = 0
    pos.pose.orientation.y = 0
    pos.pose.orientation.z = 0
    pos.pose.orientation.w = 0

    pub.publish(pos)
