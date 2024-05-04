#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 15:53:15 2024

@author: claremalhotra
"""


def gcd(a, b):
    """
    This function calculates the greatest common divisor between two numbers
    """
    x = [a, b]
    a2, b2 = sorted(x)
    if b == 0:
        return a
    return gcd(b, a % b)


def remove_pairs(dir_string):
    """
    This function removes turnaround pairs from a direction string
    """
    if len(dir_string) <= 1:
        return dir_string
    if "NS" in dir_string:
        a, b = dir_string.split("NS")
        c = remove_pairs(a) + remove_pairs(b)
        return c
    elif "SN" in dir_string:
        a, b = dir_string.split("SN")
        c = remove_pairs(a) + remove_pairs(b)
        return c
    elif "WE" in dir_string:
        a, b = dir_string.split("WE")
        c = remove_pairs(a) + remove_pairs(b)
        return c
    elif "EW" in dir_string:
        a, b = dir_string.split("EW")
        c = remove_pairs(a) + remove_pairs(b)
        return c
    else:
        return dir_string


def bisection_root(fn, x1, x2):
    """
    This function calculates the root of a function given x values on either
    side of an intercept
    """
    if fn(x1) > 0 and fn(x2) > 0:
        raise ValueError("Both y values cannot be positive")
    if fn(x1) < 0 and fn(x2) < 0:
        raise ValueError("Both y values cannot be negative")
    if abs(fn(x1)) <= 10**-7:
        return x1
    if abs(fn(x2)) <= 10**-7:
        return x2
    else:
        x3 = (x1+x2)/2
        if fn(x3) > 0:
            if fn(x1) < 0:
                x4 = x1
            else:
                x4 = x2
        elif fn(x3) < 0:
            if fn(x1) > 0:
                x4 = x1
            else:
                x4 = x2
        return bisection_root(fn, x3, x4)
