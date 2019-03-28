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

    @property
    def road_id_up(self):
        return self.__road_id_up

    @property
    def road_id_right(self):
        return self.__road_id_up

    @property
    def road_id_down(self):
        return self.__road_id_up

    @property
    def road_id_left(self):
        return self.__road_id_up

    def __move_go_straight(self, graph):
        # 将车前进
        return True

    def __move_turn_left(self, graph):
        # 将车左转
        return True

    def __move_turn_right(self, graph):
        # 将车右转
        return True

    @staticmethod
    def __has_car_to_move(cars):
        flag = False
        for i in cars:
            if len(i[1]) != 0:
                flag = True
                break
        return flag

    def move(self):
        # roads = graph_data.get_cross_direction()
        # cars = [[road, road.get_cross_car(self)] for road in roads]
        # while Cross.__has_car_to_move(cars):
        #     # 判断车的移动
        #     cars = [[road, road.get_cross_car(self)] for road in roads]
        pass
