#! /usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import numpy as np
vel_msg = Twist()
angular_speed = 0.017
dist = 0.0

def veloc():
   pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
   rospy.init_node('velocity', anonymous=True)
   rate = rospy.Rate(10) # 10hz
   while not rospy.is_shutdown():
        angular_speed = 0.3
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0
	
	dist = rospy.get_param('distance')
	if(dist > 0.5):

			if ((int(rospy.get_param('angle')) < -10)):
			     vel_msg.angular.z = -angular_speed
			     pub.publish(vel_msg)
			     rate.sleep()
			else:
				if ((int(rospy.get_param('angle')) > 10)):
					vel_msg.angular.z = angular_speed
					pub.publish(vel_msg)
					rate.sleep()
		     		else:
					vel_msg.linear.x = 1
					vel_msg.angular.z = 0
					pub.publish(vel_msg)
					rate.sleep()
		
	else:
		vel_msg.linear.x = 0
		vel_msg.angular.z = 0
		pub.publish(vel_msg)
		rate.sleep()


if __name__ == '__main__':
  try:
    veloc()
  except rospy.ROSInterruptException:
    pass

rospy.init_node('velocity')
#sub = rospy.Subscriber(rospy.get_param('scan_subscriber_topic_name'), LaserScan, callback)
rospy.spin()

  

  
