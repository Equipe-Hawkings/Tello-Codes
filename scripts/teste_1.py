#!/usr/bin/env python3
import rospy
from tello_control.control import Control


class Drone(Control):
    def __init__(self):
        Control.__init__(self)

    def voo(self):
        for i in range(3):
            self.decolar()
        self.pousar()

if __name__ == "__main__":
   try:
      rospy.init_node('mission', anonymous=True)
      Interprise = Drone()
      Interprise.voo()
   except rospy.ROSInterruptException:
      pass