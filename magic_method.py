#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :magic method
@Date     :2021/04/30 08:07:40
@Author      :xbMa
'''

import collections

from random import choice

'''
 __init__ initial object
 __str__  provide readable output
 __repr__ provide definite output, use repr() can call it
 '''
class Person():

    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def __str__(self):
        return f"{self.name} is {self.occupation}"

    def __repr__(self):
        return '<{0}.{1} object at {2}>'.format(self.__module__, type(self).__name__, hex(id(self)))

p = Person("xbMa", "engineer")
print(p)
print(repr(p))


'''
__len__     return container length, use len() can call it
__getitem__ define project request []
'''
Cards = collections.namedtuple('Cards', ['suit', 'rank'])

class Poker():
    ranks = [str(i) for i in range(2,11)] + list('JQKA')
    suits = ["heart", "clubs", "spades", "diamond"]

    def __init__(self):
        self.total = [Cards(suit, rank) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.total)

    def __getitem__(self, index):
        return self.total[index]

poker = Poker()
print(len(poker))
print(choice(poker))