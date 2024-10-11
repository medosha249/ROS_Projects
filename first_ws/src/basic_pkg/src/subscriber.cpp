#include <ros/ros.h>
#include <std_msgs/String.h>

void chatterCallback(const std_msgs::String::ConstPtr &msg)
{

    ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{

    ros::init(argc, argv, "subscriber");
    ros::NodeHandle nh;

    ros::Subscriber chatter_sub = nh.subscribe("chatter", 50, chatterCallback);

    ros::spin();
    return 0;
}
