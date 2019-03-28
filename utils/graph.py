# -*- coding: utf-8 -*-
"""
* @Author: ziuno
* @Software: PyCharm
* @Time: 2019/3/27 20:39
"""


class Graph(object):

    def __init__(self):
        self.__roads = []
        self.__crosses = []

    def set_road(self, road):
        self.__roads.append(road)

    def set_cross(self, cross):
        self.__crosses.append(cross)
