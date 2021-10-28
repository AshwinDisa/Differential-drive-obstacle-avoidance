#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


def callback(scan_data):

	global ranges
	ranges = scan_data.ranges

def move(speed):

	velocity_message = Twist()
	velocity_message.linear.x = abs(speed)
	velocity_message.angular.z = 0.0
	loop_rate = rospy.Rate(20)
	threshold = 0.75
	while ranges[360] > threshold and ranges[345] > threshold and ranges[375] > threshold:
		print("---------------")
		print("Moving Straight")
		print("---------------")
		pub.publish(velocity_message)
		loop_rate.sleep()
	rotate(1.5)

def rotate(ang_speed):

	velocity_message = Twist()
	velocity_message.angular.z = abs(ang_speed)
	velocity_message.linear.x = 0.0
	loop_rate = rospy.Rate(20)
	threshold = 0.75
	while ranges[360] < threshold or ranges[345] < threshold or ranges[375] < threshold:
		print("---------------")
		print("Rotating")
		print("---------------")
		pub.publish(velocity_message)
		loop_rate.sleep()
	move(0.4)

if __name__ == "__main__":
	try:
		rospy.init_node("avoidance_node")
		pub_topic_name = "/cmd_vel"
		sub_topic_name = "/scan"
		pub = rospy.Publisher(pub_topic_name, Twist, queue_size = 10)
		sub = rospy.Subscriber(sub_topic_name, LaserScan, callback)
		rospy.sleep(10)
		move(0.4)
		rospy.spin()

	except rospy.ROSInterruptException:
		rospy.loginfo('ROS node terminated')