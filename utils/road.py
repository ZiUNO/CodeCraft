# -*- coding: utf-8 -*-
"""
* @Author: ziuno
* @Software: PyCharm
* @Time: 2019/3/27 21:05
"""
from car import Car
from cross import Cross


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
        self.__roads.append([])  # start->end
        if is_duplex is True:
            self.__roads.append([])  # end->start
        for i in range(len(self.__roads)):
            for _ in range(channel):
                self.__roads[i].append([0] * length)

    def set_car_by_pos(self, pos, car, start_to_end=True, remaining_step=0):
        if not self.__is_duplex and not start_to_end:
            return False
        i = 0
        direction = 0 if start_to_end else 1
        while i < self.__channel and self.__roads[direction][i][-1] != 0:
            i += 1
        if i == self.__channel:
            return False
        car.remaining_step = remaining_step
        car.has_moved = True
        self.__roads[start_to_end][i][pos] = car
        return True

    @property
    def id(self):
        return self.__id

    @property
    def end(self):
        return self.__end
    @end.setter
    def end(self, end):
        self.__end = end
    @property
    def start(self):
        return self.__start
    @start.setter
    def start(self, start):
        self.__start = start

    def del_car(self, car, start_to_end=True):
        if not self.__is_duplex and not start_to_end:
            return False
        direction = 0 if start_to_end else 1
        for i in range(self.__channel):
            if self.__roads[direction][i].count(car) != 0:
                index = self.__roads[direction][i].index(car)
                self.__roads[direction][i][index] = 0
                return True
        return False

    def update(self):
        for side in self.__roads:
            for i in range(self.__channel):
                road = side[i]
                for pos, tmp_car in enumerate(road):
                    if tmp_car == 0:
                        continue
                    tmp_step = tmp_car.remaining_step
                    if tmp_step == 0:
                        continue
                    tmp_pos = pos
                    while tmp_pos != 0 and road[tmp_pos - 1] == 0 and tmp_step != 0:
                        tmp_pos -= 1
                        tmp_step -= 1
                    road[pos].has_moved = False
                    road[tmp_pos] = road[pos]
                    road[pos] = 0
                side[i] = road

    def get_cross_car(self, cross):
        cross_car = []
        direction = 1 if cross.id == self.__start else 0
        for i in range(self.__channel):
            for tmp in self.__roads[direction][i]:
                if tmp != 0 and not tmp.has_moved:
                    cross_car.append(tmp)
                    break
        return cross_car

    def print(self):
        for side in self.__roads:
            for i in range(self.__channel):
                print(i, side[i])


if __name__ == '__main__':
    cross = Cross(3, 5002, 5009, 5001, -1)
    cross2 = Cross(4, 5003, 5010, 5002, -1)
    car = Car(10004, 38, 5, 4, 4)
    car2 = Car(10004, 38, 5, 4, 4)
    road = Road(5002, 20, 4, 3, 3, 4, True)
    road.set_car_by_pos(5, car, remaining_step=1)
    road.set_car_by_pos(6, car2, remaining_step=5)
    road.print()
    road.update()
    road.print()
    print(road.get_cross_car(cross))
    print(road.get_cross_car(cross2))
