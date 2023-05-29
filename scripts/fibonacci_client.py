#!/usr/bin/env python3

from __future__ import print_function

import sys
import rospy
from beginner_tutorials.srv import *

def fibonacci_client(n):
    rospy.wait_for_service('fibonacci')
    try:
        fibonacci = rospy.ServiceProxy('fibonacci', Fibonacci)
        resp1 = fibonacci(n)
        return resp1.fib
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    n = int(sys.argv[1])
    
    print("Requesting " + str(n) + "th fibonacci number ")
    print(fibonacci_client(n))