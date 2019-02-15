#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
import numpy as np


value = 0
index = 0
maxi = 0		##max and min angles for scan sensor
mini = 0
auxi = 0

def callback(msg):
  #obtain the minimun
  value = 30.0
  index = 0
  for i in range(10, 709):
    if (msg.ranges[i] < 30.0):		#max range is 30m
	if (msg.ranges[i] < value):
		value = msg.ranges[i]
		index = i

  maxi = rospy.get_param('scan_max_angle')
  mini = rospy.get_param('scan_min_angle')
  maxi = int(maxi)
  mini = int(mini)
  auxi = np.divide((maxi-mini),720.0)
  auxi = (np.multiply(auxi, index)) + mini
  rospy.set_param('angle', int(auxi) )
  print value
  #print index
  print (rospy.get_param('angle'))
  rospy.set_param('distance', value)

rospy.init_node('scan_values')
sub = rospy.Subscriber(rospy.get_param('scan_sub_topic'), LaserScan, callback)
rospy.spin()

