#!/usr/bin/env python 3.8
import rospy
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist

safe_Distance = 0.3
cmd_vel_pub=None

def ultrasonic_callback(msg):
    global cmd_vel_pub
    twist = Twist()

    if msg.range < safe_Distance:
        rospy.loginfo("Obstacle Destected! ..... STOPING THE ROBOT....")
        twist.linear.x=0.0
        twist.angular.z = 1
    else:
        twist.linear.x = 1
        twist.angular.z = 1

    cmd_vel_pub.publish(twist)

def main():
    global cmd_vel_pub
    rospy.init_node("obstacle_avoidence")
    rospy.Subscriber("/ultrasonic1" ,Range , ultrasonic_callback)
    rospy.Subscriber("/ultrasonic2",Range , ultrasonic_callback)
    cmd_vel_pub = rospy.Publisher("/cmd_vel" ,Twist , queue_size=10)
    rospy.spin()

if __name__ == "__main__":
    main()
