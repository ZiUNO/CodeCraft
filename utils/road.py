# -*- coding: utf-8 -*-
"""
* @Author: ziuno
* @Software: PyCharm
* @Time: 2019/3/27 21:05
"""
from utils.car import Car
from utils.cross import Cross


class Road(object):
    LEFT = 0
    RIGHT = 1

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

    def append_car_by_step(self, car, step, cross, left_or_right=RIGHT):
        if not self.__is_duplex and cross.id == self.__end and left_or_right == Road.RIGHT:
            return False
        i = 0
        direction = 1 if (left_or_right == Road.LEFT and cross.id == self.__start) or (
                left_or_right == Road.RIGHT and cross.id == self.__end) else 0
        while i < self.__channel and self.__roads[direction][i][-1] != 0:
            i += 1
        if i == self.__channel:
            return False
        tmp_road = list(reversed(self.__roads[direction][i]))
        for j, item in enumerate(tmp_road):
            step -= 1
            if step == 0:
                car.remaining_step = 0
                tmp_road[j] = car
                break
            elif j == len(tmp_road) - 1:
                car.remaining_step = step
                tmp_road[j] = car
                break
            elif tmp_road[j + 1] != 0:
                car.remaining_step = step
                tmp_road[j] = car
                break
        car.has_moved = True
        self.__roads[direction][i] = list(reversed(tmp_road))
        return True

    def move_car_by_step(self, car, step):
        for i, roads in enumerate(self.__roads):
            for j, road in enumerate(roads):
                if road.count(car) == 0:
                    continue
                tmp_road = self.__roads[i][j]
                tmp_road = list(reversed(tmp_road))
                index = tmp_road.index(car)
                tmp_road[index] = 0
                while index != len(tmp_road) - 1 and tmp_road[index + 1] == 0 and step != 0:
                    index += 1
                    step -= 1
                car.has_moved = True
                tmp_road[index] = car
                self.__roads[i][j] = list(reversed(tmp_road))
                return True
        return False

    @property
    def speed(self):
        return self.__speed

    @property
    def id(self):
        return self.__id

    def del_car(self, car):
        for i, roads in enumerate(self.__roads):
            for j, road in enumerate(roads):
                if road.count(car) == 0:
                    continue
                index = road.index(car)
                self.__roads[i][j][index] = 0
                return True
        return False

    def update(self):
        for j, side in enumerate(self.__roads):
            for k in range(self.__channel):
                road = side[k]
                for pos, tmp_car in enumerate(road):
                    if tmp_car == 0:
                        continue
                    tmp_step = tmp_car.remaining_step
                    if tmp_step == 0:
                        tmp_car.has_moved = False
                        continue
                    tmp_pos = pos
                    car = self.__roads[j][k][pos]
                    while tmp_pos != 0 and road[tmp_pos - 1] == 0 and tmp_step != 0:
                        tmp_pos -= 1
                        tmp_step -= 1
                    car.has_moved = False
                    road[pos] = 0
                    road[tmp_pos] = car
                side[k] = road

    def get_cross_car(self, cross):
        cross_car = []
        direction = 1 if cross.id == self.__start else 0
        for road in self.__roads[direction]:
            for car in road:
                if car != 0 and not car.has_moved:
                    cross_car.append(car)
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
    road.append_car_by_step(car, 9, cross)
    road.append_car_by_step(car2, 5, cross)
    road.print()
    road.update()
    road.print()
    road.move_car_by_step(car, 3)
    road.print()
    print(road.get_cross_car(cross))
    print(road.get_cross_car(cross2))
    road.update()
    print(road.get_cross_car(cross))
    print(road.get_cross_car(cross2))
