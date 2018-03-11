#!/usr/bin/env python

from srvserverclient.srv import *
import rospy

def mc_init():
    print "mc initialized on mc_command server"
    return srvcommResponse(True)

def mc_start():
    print "mc started on mc_command server"
    return srvcommResponse(True)

def mc_invalid():
    print "command invalid on mc_command server"
    return srvcommResponse(False)

def mc_command_handler():
    # switch = {
    #     'init' : mc_init,
    #     'start': mc_start,   
    #     # 'default': mc_invalid
    # }
    
    # switch[arg]
    return srvcommResponse(False)

def handle_mc_commands(req):
    switcher = {
        'init': mc_init,
        'start': mc_start        
    }
    func = switcher.get(req.command, 'mc_invalid')

    return func()

def mc_command_server():
    rospy.init_node('mc_command_server')
    mc_server_ = rospy.Service('mc_command', srvcomm, handle_mc_commands)
    print 'ready to received mc commands'
    rospy.spin()


if __name__ == '__main__':
    mc_command_server()