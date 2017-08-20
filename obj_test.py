#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def __init__(self, name):
        self.name = name

    second_surnmae = "justin"
    __slots__ = ('sid','name','ba')


a = Animal('aa')
Animal.surname = "aanikle"
print(a)
print(Animal.surname)
print(a.surname)
print(Animal.second_surnmae)
print(a.second_surnmae)


from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


def member_func(self, name='world'):
    print(name)
    


New_Class = type('NewClass', (object,), dict(func = member_func))

h = New_Class()
print(h)
