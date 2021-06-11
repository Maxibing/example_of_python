#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :Usage of @property
@Date     :2021/06/10 21:45:03
@Author      :xbMa
'''

class state():

    def __init__(self):
        self._number = None

    # Read only
    @property
    def number(self):
        return self._number

    # Can write
    @number.setter
    def number(self, value):
        self._number = value

    # Can delete
    @number.deleter
    def number(self):
        # del self._number
        self._number = None


if __name__ == "__main__":
    s = state()
    print(s.number)
    s.number = 3
    print(s.number)
    del s.number
    print(s.number)
