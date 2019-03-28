# -*- coding: utf-8 -*-
"""
* @Author: ziuno
* @Software: PyCharm
* @Time: 2019/3/27 21:04
"""


class Cross(object):
    def __init__(self, id, road_id_up, road_id_right, road_id_down, road_id_left):
        self.__id = id
        self.__road_id_up = road_id_up
        self.__road_id_right = road_id_right
        self.__road_id_down = road_id_down
        self.__road_id_left = road_id_left

    @property
    def id(self):
        return self.__id

    def __move_go_straight(self, graph):
        pass

    def __move_turn_left(self, graph):
        pass
