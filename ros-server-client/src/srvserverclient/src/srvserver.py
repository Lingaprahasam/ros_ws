#!/usr/bin/env python

from srvcomm.srv import *
import rospy

def handle_mc_commands():
    return srvcommResponse()

def mc_command_server():
    rospy.init_node('mc_command_server')
    mc_server_ = rospy.Service('mc_command', srvcomm, handle_mc_commands)
    print 'ready to received mc commands'
    rospy.spin()


if __name__ == "__main__"
    mc_command_server()