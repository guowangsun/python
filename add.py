#!/usr/bin/env python
# -*- coding: utf-8 -*-
def my_add(x, y):
    return x + y
sum = 0
for x in range(101):
    sum = my_add(sum, x)
print sum
