#!/usr/bin/env python
# _*_ conding: utf-8 _*_

v = map(int, raw_input().split())
if not v[0] % v[1]:
    print 'YES'
else:
    print 'NO'
