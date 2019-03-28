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
        self.__roads = []
        self.__roads.append([list()] * channel)  # start->end
        if is_duplex is True:
            self.__roads.append([list()] * channel)  # end->start

    def set_car_by_pos(self, pos, car, start_to_end=True, remaining_step=0):
        if not self.__is_duplex and start_to_end == 1:
            return False
        i = 0
        while self.__roads[start_to_end][i][-1] == 0 and i < self.__channel:
            i += 1
        if i == self.__channel:
            return False
        car.remaining_step = remaining_step
        self.__roads[start_to_end][i][pos] = car
        return True

    def del_car(self, car, start_to_end=True):
        if not self.__is_duplex and start_to_end == 1:
            return 0

    def update(self):
        pass

    def get_go_straight(self):
        go_straight = []
        return go_straight

    def get_turn_left(self):
        turn_left = []
        return turn_left

    def get_turn_right(self):
        turn_right = []
        return turn_right
