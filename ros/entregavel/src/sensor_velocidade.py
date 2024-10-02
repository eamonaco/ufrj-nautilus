#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Point
import random
import time

rospy.init_node('sensor_velocidade')

pub = rospy.Publisher('/velocidade', Point, queue_size=10)

while not rospy.is_shutdown():
    velocidade = Point()
    velocidade.x = 3
    velocidade.y = 2
    velocidade.z = 1
    
    pub.publish(velocidade)
    time.sleep(5)