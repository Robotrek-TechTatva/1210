#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
class Bruh:
    def __init__(self):
        self.b1=0
        self.b2 =0
        sub1 = rospy.Subscriber('/bruh1',Int32,self.cb1)
        sub2 = rospy.Subscriber('/bruh2',Int32,self.cb2)
        self.pub = rospy.Publisher('/sum',Int32,queue_size=10)


    def cb1(self,msg):
        self.b1 = msg.data
        print("Bruh1: "+str(msg.data))
    def cb2(self,msg):
        self.b2 = msg.data
        sum = self.b1+self.b2
        
        print("Bruh2: "+str(msg.data))
	print("Sum = "+str(sum))

        self.pub.publish(sum)

if __name__ =="__main__":
    rospy.init_node('Bruh_sub')

    r=Bruh()

    rospy.spin()
