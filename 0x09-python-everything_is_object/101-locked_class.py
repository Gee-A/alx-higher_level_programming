#!/usr/bin/python3
class LockedClass:

    __slots__ == ['firs_name']

    def __init__(self, firs_name=''):
        self.firs_name = firs_name
