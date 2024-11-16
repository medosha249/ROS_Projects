#include<ros/ros.h>
#include<geometry_msgs/Twist.h>


int main(int argc,char** argv){
    ros::init(argc , argv ,"control_sparkbot");
    ros::NodeHandle nh;
    ros::Publisher control;
    control = nh.advertise<geometry_msgs::Twist>("/sparkbot/cmd_vel", 10);
    ros::Rate rate(10);
    geometry_msgs::Twist control_vel;
    
        control_vel.linear.x=5;
        control_vel.linear.y=0;
        control_vel.linear.z=0;
        control_vel.angular.x=0;
        control_vel.angular.y=0;
        control_vel.angular.z=1;
    while(ros::ok()){
        control.publish(control_vel);
        ros::spinOnce();
        rate.sleep();
        
    }

    
}