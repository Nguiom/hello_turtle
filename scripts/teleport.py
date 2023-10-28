#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import TeleportAbsolute Teleport

class Teleport(self):
	def __init__(self): 
		rospy.init_node('Teleport', anonymous=False)
        	self.pose_sub = rospy.Subscriber('/turtle1/pose',Pose, self.update_pose)
		self.key_sub= rospy.Subscriber('key',Pose, self.update_key)
		self.pose=Pose()
		self.key=0
		self.tabla={' ':(1),'r':(2)}
		while not rospy.is_shutdown():
			rospy.spin()
			if(self.tabla==1):
				teleportA(self.pose.x,self.pose.y,self.pose.theta+3.1416)
			elif(self.tabla==2):
				teleportA(5,5,0)
	def teleportA(self,x,y,angle):
		rospy.wait_for_service('/turtle1/teleport_absolute')
		try:
        		teleportA = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        		resp1 = teleportA(x, y, angle)
        		print('Teleported to x: {}, y: {}, ang: {}'.format(str(x),str(y),str(angle)))
   		 except rospy.ServiceException as e:
        		print(str(e))
	def update_pose(self,data):
		self.pose=data
	def update_key(self,data):
		self.key=self.tabla.get(data,(0))

if __name__== "__main__": 
    try:
        Teleport() 
    except: 
    	rospy.loginfo("End of the trip for Turtlesim") 