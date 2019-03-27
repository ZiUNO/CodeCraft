# -*- coding: utf-8 -*-
"""
* @Author: ziuno
* @Software: PyCharm
* @Time: 2019/3/27 21:05
"""


class Road(object):
    def __init__(self, id, length, speed, channel, start, end, is_duplex):
        self.__id = id
        self.__length = length
        self.__speed = speed
        self.__channel = channel
        self.__start = start
        self.__end = end
        self.__is_duplex = is_duplex
