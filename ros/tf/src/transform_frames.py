#!/usr/bin/python3

import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped
import math

rospy.init_node('sun_earth_broadcaster')

def orbit_transform(child, header):
    
    # Tempo será usado no cálculo do ângulo para as funções trigonométricas
    time = rospy.Time.now().to_sec()
    
    # Pega os parâmetros da órbita do servidor
    orbit = rospy.get_param(f'{child}_{header}') 
    semiradius_x = orbit[0]
    semiradius_y = orbit[1]
    sense = orbit[2]
    angular_velocity = orbit[3]  

    # Cálculo do ângulo theta
    theta = angular_velocity * time

    # Define as coordenadas da transformação
    t = TransformStamped()
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = header
    t.child_frame_id = child

    t.transform.translation.x = sense * semiradius_x * math.sin(theta)  # O sentido da órbita é definido pela variável x
    t.transform.translation.y = semiradius_y * math.cos(theta)
    t.transform.translation.z = 0

    t.transform.rotation.x = 0
    t.transform.rotation.y = 0
    t.transform.rotation.z = 0
    t.transform.rotation.w = 1

    return t

broad = tf2_ros.TransformBroadcaster()

while not rospy.is_shutdown():
    
    # Cria as transformadas dos planetas
    
    t_1 = orbit_transform("mercury", "sun")
    t_2 = orbit_transform("venus", "sun")
    t_3 = orbit_transform("earth", "sun")
    t_4 = orbit_transform("mars", "sun")
    t_5 = orbit_transform("jupiter", "sun")
    t_6 = orbit_transform("saturn", "sun")
    t_7 = orbit_transform("uranus", "sun")
    t_8 = orbit_transform("neptune", "sun")
    
    # Transformadas dos satélites

    t_9 = orbit_transform("moon", "earth")

    # Manda as transformadas
    
    broad.sendTransform(t_1)
    broad.sendTransform(t_2)
    broad.sendTransform(t_3)
    broad.sendTransform(t_4)
    broad.sendTransform(t_5)
    broad.sendTransform(t_6)
    broad.sendTransform(t_7)
    broad.sendTransform(t_8)
    broad.sendTransform(t_9)

    
