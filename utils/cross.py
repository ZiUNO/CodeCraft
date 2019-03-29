# -*- coding: utf-8 -*-
"""
* @Author: ziuno
* @Software: PyCharm
* @Time: 2019/3/27 21:04
"""
from utils.car import Car
from utils.graph import Graph


class Cross(object):
    STRAIGHT = 2
    LEFT = 1
    RIGHT = 3
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def __init__(self, id, road_id_up, road_id_right, road_id_down, road_id_left):
        self.__id = id
        self.__road_id_up = road_id_up
        self.__road_id_right = road_id_right
        self.__road_id_down = road_id_down
        self.__road_id_left = road_id_left
        self.__graph = 0
        self.LEFT = 1
        self.STRAIGHT = 2
        self.RIGHT = 3
        self.xy = None

    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, graph):
        self.__graph = graph

    @property
    def xy(self):
        return self.__xy

    @xy.setter
    def xy(self, xy):
        self.__xy = xy

    @property
    def id(self):
        return self.__id

    @property
    def road_id_up(self):
        return self.__road_id_up

    @property
    def road_id_right(self):
        return self.__road_id_right

    @property
    def road_id_down(self):
        return self.__road_id_down

    @property
    def road_id_left(self):
        return self.__road_id_left

    # 判断路在当前路口的位置
    def __get_road_pos_to_cross(self, road):
        return self.graph.graDic[self.id].index(road.id)

    # 根据当前道路和转弯方向获取下一条路
    def __get_road_by_direction(self, road, turn):
        roadList = self.graph.get_roads(self)
        nextRoad = roadList[(roadList.index(road) + turn) % 4]

        return nextRoad

    def __move_go_straight(self, road, car):
        # 根据车的属性move_way将车前进
        if car.move_way[1] == 0:
            road.move_car_by_step(car, car.move_way[0])
        else:

            if road.del_car(car):

                nextRoad = self.__get_road_by_direction(road, self.STRAIGHT)
                nextRoad.append_car_by_step(car, car.move_way[0], self)
            else:
                return False

        return True

    def __move_turn_left(self, road, car):
        # 根据车的属性move_way将车左转
        if road.del_car(car):
            nextRoad = self.__get_road_by_direction(road, self.LEFT)
            nextRoad.append_car_by_step(car, car.move_way[1], self)
        else:
            return False
        return True

    def __move_turn_right(self, road, car):
        # 根据车的属性move_way将车右转
        if road.del_car(car):
            nextRoad = self.__get_road_by_direction(road, self.RIGHT)
            nextRoad.append_car_by_step(car, car.move_way[1], self)
        else:
            return False

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
        direction = Car.GO_STRAIGHT
        now_speed = min(car.speed, road.speed)
        left_road = self.__get_road_by_direction(road, Cross.LEFT)
        right_road = self.__get_road_by_direction(road, Cross.RIGHT)
        straight_road = self.__get_road_by_direction(road, Cross.STRAIGHT)
        left_speed = min(car.speed, left_road.speed)
        straight_speed = min(car.speed, straight_road.speed)
        right_speed = min(car.speed, right_road.speed)
        spare_place, have_front_car = road.spare_place(car)
        aim_direction = self.__graph.get_end_direction(car, self)
        now_road_pos = self.__get_road_pos_to_cross(road)
        if have_front_car or spare_place > now_speed:
            road.move_car_by_step(car, now_speed)
        else:
            left_step = 0 if spare_place >= left_speed else left_speed - spare_place
            right_step = 0 if spare_place >= right_speed else right_speed - spare_place
            straight_step = 0 if spare_place >= straight_speed else straight_speed - spare_place
            left_step = road.append_car_by_step(car, left_step, self, feeler=True) if left_step != 0 else 0
            right_step = road.append_car_by_step(car, right_step, self, feeler=True) if right_step != 0 else 0
            straight_step = road.append_car_by_step(car, straight_step, self, feeler=True) if straight_step != 0 else 0

            all_step = [left_step, straight_step, right_step]
            directions = []
            for i in aim_direction:
                if aim_direction[i] == 1:
                    directions.append((i - now_road_pos) % 4)
            steps = []
            for tmp in directions:
                if tmp == Cross.STRAIGHT:
                    steps.append((all_step[1], Cross.STRAIGHT))
                elif tmp == Cross.LEFT:
                    steps.append((all_step[0], Cross.LEFT))
                elif tmp == Cross.RIGHT:
                    steps.append((all_step[2], Cross.RIGHT))
            steps.sort(reverse=True)
            final = steps[0]
            car.move_way = [spare_place, final[0]]
            car.direction = final[1]
            direction = car.direction
        return direction

    def __get_sort_road_car(self, road_cars):
        road_car = []
        for item in road_cars:
            road, cars = item
            for car in cars:
                road_car.append([self.__judge_direction_and_distance(car, road), car, road])
        road_car.sort()
        return road_car

    def move(self):
        roads = self.__graph.get_roads()  # 获得图的当前cross的链接的道路的列表
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


if __name__ == '__main__':
    graph = Graph()
    cross = Cross(3, 5002, 5009, 5001, -1)
    cross.graph = graph
