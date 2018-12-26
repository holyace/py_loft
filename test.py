#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
create by:chad at 2018/12/24

"""

from net import easy_net

url = "http://www.baidu.com/s"
params = {"wd": "pic"}
resp = easy_net.get(url, None, params)
print(resp)
