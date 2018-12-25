#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
create by:chad at 2018/12/24

"""


def test(in_list):
    for i in range(10):
        in_list.append(i)
    return


def print_list(in_list):
    for i in in_list:
        print(type(i), i)


list_a = []
print("id:", id(list_a))
test(list_a)
print("id:", id(list_a))
print_list(list_a)
