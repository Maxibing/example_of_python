#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :usage of print cover multi lines
@Date     :2021/06/08 21:17:22
@Author      :xbMa
'''

def put_cursor(x,y):
    print("\x1b[{};{}H".format(y+1,x+1))

def clear():
    print("\x1b[2J")

clear()
put_cursor(0,0)
print("hello")
print("huhu")

#return to first line
put_cursor(0,0)
print("noooooo")