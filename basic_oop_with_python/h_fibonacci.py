#!/usr/bin/python
''' Returns nth fibnaocci number '''
def fibonacci(n):
    n1=0
    n2=1
    for i in range(0,n):
        temp=n1
        n1=n2
        n2=temp+n1
    return n1
        
