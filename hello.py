#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
name = raw_input('Please enter your name : ')
print 'Hello,', name
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
