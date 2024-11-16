#!/usr/bin/python3.8

import rospy
from geometry_msgs.msg import Twist
import sys
import termios
import tty

def get_key():
    """
    Reads a single character from standard input (non-blocking).
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

def main():
    rospy.init_node('teleop_twist_keyboard')

    # Define the publisher
    pub = rospy.Publisher('/sparkbot/cmd_vel', Twist, queue_size=10)

    # Create a Twist message
    cmd = Twist()

    print("Control the robot with w/a/s/d keys. Press 'x' to stop and 'q' to quit.")

    # Loop to capture keypresses
    while not rospy.is_shutdown():
        key = get_key()

        # Define the linear and angular velocities based on key press
        if key == 'w':
            cmd.linear.x = 5  # Move forward
            cmd.angular.z = 0.0
        elif key == 's':
            cmd.linear.x = -5  # Move backward
            cmd.angular.z = 0.0
        elif key == 'a':
            cmd.linear.x = 0.0
            cmd.angular.z = 2  # Turn left
        elif key == 'd':
            cmd.linear.x = 0.0
            cmd.angular.z = -2  # Turn right
        elif key == 'x':
            cmd.linear.x = 0.0  # Stop moving forward/backward
            cmd.angular.z = 0.0  # Stop rotating
        elif key == 'q':
            print("Exiting teleop control.")
            break
        else:
            # Ignore unknown keys
            continue

        # Publish the velocity command
        pub.publish(cmd)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
    except KeyboardInterrupt:
        print("\nTeleop interrupted.")
