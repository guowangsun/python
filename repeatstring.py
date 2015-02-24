#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import codecs
from collections import defaultdict

file = raw_input('Please file: ')
spliter = raw_input('Please spliter: ')
if spliter == '':
    spliter = ' '
d = defaultdict(lambda: 0)

with codecs.open(file, 'r', 'utf-8') as f:
    str = f.read()

for x in [s.lower() for s in str.split(spliter)]:
    d[x] = d[x] + 1

for x, y in d.iteritems():
    if y == 2:
        print x, y

