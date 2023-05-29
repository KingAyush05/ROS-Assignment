#!/usr/bin/env python3

from __future__ import print_function

from beginner_tutorials.srv import Fibonacci,FibonacciResponse
import rospy

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_handler(req):
    print("Returning %sth fibonacci number"%(req.n))
    n = req.n

    fib=fibonacci(n)
    
    return FibonacciResponse(fib)

def fibonacci_server():
    rospy.init_node('fibonacci_server')
    s = rospy.Service('fibonacci', Fibonacci, fibonacci_handler)
    print("Ready to calculate nth fibonacci number.")
    rospy.spin()

if __name__ == "__main__":
    fibonacci_server()