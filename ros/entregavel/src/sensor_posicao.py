#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Point
# from random import randint
import time

rospy.init_node('sensor_posicao')

pub = rospy.Publisher('/posicao', Point, queue_size=10)

while not rospy.is_shutdown():
    ponto = Point()
    ponto.x = 1
    ponto.y = 2
    ponto.z = 3

    pub.publish(ponto)
    time.sleep(5)