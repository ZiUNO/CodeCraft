# -*- coding: utf-8 -*-
"""
* @Author: ziuno
* @Software: PyCharm
* @Time: 2019/3/27 21:04
"""
from utils.car import Car
from utils.graph import Graph


class Cross(object):

    def __init__(self, id, road_id_up, road_id_right, road_id_down, road_id_left):
        self.__id = id
        self.__road_id_up = road_id_up
        self.__road_id_right = road_id_right
        self.__road_id_down = road_id_down
        self.__road_id_left = road_id_left
        self.__graph = 0

    @property
    def graph(self, graph):
        self.__graph = graph

    @graph.setter
    def graph(self, graph):
        self.__graph = graph

    @property
    def id(self):
        return self.__id

    def __move_go_straight(self, road, car):
        # 根据车的属性move_way将车前进
        return True

    def __move_turn_left(self, road, car):
        # 根据车的属性move_way将车左转
        return True

    def __move_turn_right(self, road, car):
        # 根据车的属性move_way将车右转
        return True

    @staticmethod
    def __has_car_to_move(cars):
        flag = False
        for i in cars:
            if len(i[1]) != 0:
                flag = True
                break
        return flag

    def __judge_direction_and_distance(self, car, road):
        # 判断方向并在car内设置属性方向和前进move_way的值
        return Car.GO_STRAIGHT

    def __get_sort_road_car(self, road_cars):
        road_car = []
        for item in road_cars:
            road, cars = item
            for car in cars:
                road_car.append([self.__judge_direction_and_distance(car, road), car, road])
        road_car.sort()
        return road_car

    def move(self):
        roads = self.__graph.get_cross_direction()  # 获得图的当前cross的链接的道路的列表
        road_cars = [[road, road.get_cross_car(self)] for road in roads]
        while Cross.__has_car_to_move(road_cars):
            road_cars = [[road, road.get_cross_car(self)] for road in roads]
            road_car = self.__get_sort_road_car(road_cars)
            for item in road_car:
                i, road, car = item
                if i == Car.GO_STRAIGHT:
                    self.__move_go_straight(road, car)
                    continue
            road_cars = [[road, road.get_cross_car(self)] for road in roads]
            road_car = self.__get_sort_road_car(road_cars)
            for item in road_car:
                i, road, car = item
                if i == Car.GO_STRAIGHT:
                    break
                if i == Car.TURN_LEFT:
                    self.__move_turn_left(road, car)
                    continue
            else:
                continue
            road_cars = [[road, road.get_cross_car(self)] for road in roads]
            road_car = self.__get_sort_road_car(road_cars)
            for item in road_car:
                i, road, car = item
                if i in [Car.GO_STRAIGHT, Car.TURN_LEFT]:
                    break
                if i == Car.TURN_RIGHT:
                    self.__move_turn_right(road, car)
                    continue
