#!/usr/bin/python3.8

import rospy
from geometry_msgs.msg import Twist

def teleop_callback(key):

    cmd = Twist()

    if key == 'w':
        cmd.linear.x = 0.5  # Move forward
    elif key == 's':
        cmd.linear.x = -0.5  # Move backward
    elif key == 'a':
        cmd.angular.z = 0.5  # Turn left
    elif key == 'd':
        cmd.angular.z = -0.5  # Turn right
    elif key == 'x':
        cmd.linear.x = 0.0  # Stop moving forward/backward
        cmd.angular.z = 0.0  # Stop rotating
    return cmd

def main():
    rospy.init_node('teleop_twist_keyboard')

    pub = rospy.Publisher('/sparkbot/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(10)  # 10 Hz
    while not rospy.is_shutdown():
        key = input("Press w/s/a/d to control sparkbot, x to stop: ")
        cmd = teleop_callback(key)
        pub.publish(cmd)

        rate.sleep()

if __name__ == '__main__':
    main()
