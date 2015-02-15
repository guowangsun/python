#!/usr/bin/env python
# _*_ coding: utf-8 -*-

# add numbers
def add(*numbers):
    sum = 0
    for x in numbers:
        sum = sum + x
    return sum

# test kw
def person(name, age, **kw):
    print 'Name : ', name, 'Age : ', age, kw


s = [1,4,5,62,3]
print add(*s)
kw = {'city' : 'beijing'}
person('guowang.sun', 21, **kw)
