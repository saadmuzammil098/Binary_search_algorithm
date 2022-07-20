# -*- coding: utf-8 -*-
"""
@author: SaadMuzammil
"""

def naive_search(l, value):
    for i in range(len(l)):
        if l[i] == value:
            return i
    return -1


def binary_search(l, value, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(l)-1
    if high < low:
        return -1
        
    midpoint = (low + high) // 2
    if l[midpoint] == value:
        return midpoint
    elif value < l[midpoint]:
        return binary_search(l, value, low, midpoint-1)
    else:
        return binary_search(l, value, midpoint+1, high)   #value> l[midpoint]

if __name__ == '__main__':
    l = [1,3,5,11,13]
    value = 13
    print(naive_search(l, value))
    print(binary_search(l, value))