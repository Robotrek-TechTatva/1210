

#include <ros/ros.h>
#include <iostream>
#include <geometry_msgs/Twist.h>  
#include <stdlib.h> 
using namespace std;

int main(int argc, char **argv) {
  
	ros::init(argc, argv, "publish_velocity");
	ros::NodeHandle nh;

  
  ros::Publisher pub = nh.advertise<geometry_msgs::Twist>(
    "turtle1/cmd_vel", 1000);
	int sides=6;
  
  ros::Rate rate(.75);
	int i = 0;

	
	while(ros::ok() && i++ < sides){
			
			geometry_msgs::Twist msg;
			rate.sleep();
			msg.linear.x = double(2);
			msg.angular.z = double(0);
			
			
			pub.publish(msg);	  
			
			
			ROS_INFO_STREAM("Sending random velocity command:"
							<< " linear=" << msg.linear.x
							<< " angular=" << msg.angular.z);
			
			rate.sleep();
			
			msg.linear.x = double(0);
			msg.angular.z = double(1.04);
			
			
			pub.publish(msg);
			
			
			ROS_INFO_STREAM("Sending random velocity command:"
							<< " linear=" << msg.linear.x
							<< " angular=" << msg.angular.z);   
			rate.sleep();
			}
	
		
	
} 