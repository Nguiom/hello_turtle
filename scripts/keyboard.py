#!/usr/bin/env python

import rospy
import sys
from khbit import KBHit

class ReadKey(self):
	def __init__(self): 
		rospy.init_node('Keyboard', anonymous=False)
		self.key =rospy.Publisher('key',str, queue_size=10)
		rate = rospy.Rate(10)

	while not rospy.is_shutdown():
			self.getKey()
			rate.sleep()
		
	def getKey(self):
		if(KBHit.kbhit()):
			self.last_key=KBHit.getch()
			self.key.publish(self.last_key)

if __name__== "__main__": 
    try:
        ReadKey() 
    except: 
    	rospy.loginfo("End of the trip for Turtlesim") 

