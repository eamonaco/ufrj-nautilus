#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Point
import time

rospy.init_node('controle')

pub = rospy.Publisher('/saida', Point, queue_size=10)

posicao_atual = Point()
velocidade_atual = Point()
proxima_p = Point()

def posicao(data):
    global posicao_atual
    posicao_atual = data

def velocidade(data):
    global velocidade_atual
    velocidade_atual = data

rospy.Subscriber('/posicao', Point, posicao)
rospy.Subscriber('/velocidade', Point, velocidade)

while not rospy.is_shutdown():

    print(posicao_atual)
    print(velocidade_atual)

    proxima_p.x = posicao_atual.x + velocidade_atual.x
    proxima_p.y = posicao_atual.y + velocidade_atual.y
    proxima_p.z = posicao_atual.z + velocidade_atual.z

    pub.publish(proxima_p)

    time.sleep(5)
