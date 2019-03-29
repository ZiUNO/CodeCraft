# -*- coding: utf-8 -*-
"""
* @Author: ziuno
* @Software: PyCharm
* @Time: 2019/3/27 21:05
"""
from utils.cross import Cross


class Car(object):
    UNDEFINED = 0
    GO_STRAIGHT = 1
    TURN_RIGHT = 3
    TURN_LEFT = 2

    def __init__(self, id, start, end, speed, plan_time):
        self.__id = id
        self.__start = start
        self.__end = end
        self.__speed = speed
        self.__plan_time = plan_time
        self.__remaining_step = 0
        self.__cur_pos = []
        self.__end_pos = []
        self.__has_moved = False
        self.__move_way = [0, 0]
        self.__direction = Car.UNDEFINED

    def reset_cur_end_pos(self, graph):
        self.__cur_pos = graph.get_car_start_pos(self)
        self.__end_pos = graph.get_car_end_pos(self)

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    @property
    def move_way(self):
        return self.__move_way

    @move_way.setter
    def move_way(self, move_way):
        self.__move_way = move_way

    @property
    def has_moved(self):
        return self.__has_moved

    @has_moved.setter
    def has_moved(self, has_moved):
        self.__has_moved = has_moved

    @property
    def id(self):
        return self.__id

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    @property
    def speed(self):
        return self.__speed

    @property
    def plan_time(self):
        return self.__plan_time

    @property
    def remaining_step(self):
        return self.__remaining_step

    @remaining_step.setter
    def remaining_step(self, remaining_step):
        self.__remaining_step = remaining_step

    def move_first_step(self, graph):
        startpos = graph.crossDic[self.start]
        endpos = graph.crossDic[self.end]
        dirx = startpos.road_id_up if startpos.xy[0] < endpos.xy[0] else (
            startpos.road_id_down if startpos.xy[0] > endpos.xy[0] else None)
        diry = startpos.road_id_right if startpos.xy[1] < endpos.xy[1] else (
            startpos.road_id_left if startpos.xy[1] > endpos.xy[1] else None)
        # append_car_by_step(self, car, step, cross, left_or_right=RIGHT, feeler=False)
        sel = []
        r = (startpos.road_id_up, startpos.road_id_right, startpos.road_id_down, startpos.road_id_left)
        if (not startpos.road_id_up == -1) and graph.roadDic[startpos.road_id_up].append_car_by_step(self, self.speed,
                                                                                                     startpos,
                                                                                                     Cross.RIGHT, True):
            sel.append(0)
        if (not startpos.road_id_right == -1) and graph.roadDic[startpos.road_id_right].append_car_by_step(self,
                                                                                                           self.speed,
                                                                                                           startpos,
                                                                                                           Cross.RIGHT,
                                                                                                           True):
            sel.append(1)
        if (not startpos.road_id_down == -1) and graph.roadDic[startpos.road_id_down].append_car_by_step(self,
                                                                                                         self.speed,
                                                                                                         startpos,
                                                                                                         Cross.RIGHT,
                                                                                                         True):
            sel.append(2)
        if (not startpos.road_id_left == -1) and graph.roadDic[startpos.road_id_left].append_car_by_step(self,
                                                                                                         self.speed,
                                                                                                         startpos,
                                                                                                         Cross.RIGHT,
                                                                                                         True):
            sel.append(3)
        if len(sel) == 0:
            return False
        else:
            if len(sel) > 1:
                w = [0] * len(sel)
                for i in range(len(sel)):
                    if sel[i] == 0:
                        w[i] += (endpos.xy[1] - startpos.xy[1]) / (endpos.xy[1] + startpos.xy[1]) * 0.01
                        w[i] += (1 if endpos.xy[1] > startpos.xy[1] else -1)
                        w[i] *= 1.0 - (abs(self.speed - graph.roadDic[r[sel[i]]].speed) / (
                                self.speed + graph.roadDic[r[sel[i]]].speed))
                    elif sel[i] == 1:
                        w[i] += (endpos.xy[0] - startpos.xy[0]) / (endpos.xy[0] + startpos.xy[0]) * 0.01
                        w[i] += (1 if endpos.xy[0] > startpos.xy[0] else -1)
                        w[i] *= 1.0 - (abs(self.speed - graph.roadDic[r[sel[i]]].speed) / (
                                self.speed + graph.roadDic[r[sel[i]]].speed))
                    elif sel[i] == 2:
                        w[i] += (startpos.xy[1] - endpos.xy[1]) / (endpos.xy[1] + startpos.xy[1]) * 0.01
                        w[i] += (1 if endpos.xy[1] < startpos.xy[1] else -1)
                        w[i] *= 1.0 - (abs(self.speed - graph.roadDic[r[sel[i]]].speed) / (
                                self.speed + graph.roadDic[r[sel[i]]].speed))
                    elif sel[i] == 3:
                        w[i] += (startpos.xy[0] - endpos.xy[0]) / (endpos.xy[0] + startpos.xy[0]) * 0.01
                        w[i] += (1 if endpos.xy[0] < startpos.xy[0] else -1)
                        w[i] *= 1.0 - (abs(self.speed - graph.roadDic[r[sel[i]]].speed) / (
                                self.speed + graph.roadDic[r[sel[i]]].speed))
                best = r[sel[w.index(max(w))]]
            else:
                best = r[sel[0]]
            graph.roadDic[best].append_car_by_step(self, self.speed, startpos, Cross.RIGHT, False)
            self.__isstartgo = False
            return True

# def getCarList():
#     myCarList = []
#
#     car_path = u'../car.txt'
#     mycar = read_txt.read_txt(car_path)
#     for i in mycar:
#         temp = Car(i[0], i[1], i[2], i[3], i[4])
#         myCarList.append(temp)
#
#     return myCarList
