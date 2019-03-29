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
        self.__graDic = {}
        self.__roadDic = {}
        self.__crossDic = {}

    @property
    def graDic(self):
        return self.__graDic

    @property
    def roadDic(self):
        return self.__roadDic

    @property
    def crossDic(self):
        return self.__crossDic

    def set_road(self, road):
        self.__roads.append(road)
        self.roadDic[road.id] = road

    def set_cross(self, cross):
        self.__crosses.append(cross)

        # print(cross.id)
        # print(cross.road_id_up)
        # print(cross.road_id_right)
        # print(cross.road_id_down)
        # print(cross.road_id_left)

        self.graDic[cross.id] = [cross.road_id_up, cross.road_id_right, cross.road_id_down, cross.road_id_left]
        self.crossDic[cross.id] = cross
        # print(self.__graDic)

    def get_cross(self):
        return self.__crosses

    def get_road(self):
        return self.__roads

    def update(self):
        for i in self.get_road():
            i.update()

    def get_roads(self, cross):
        temp = []
        for i in self.graDic[cross.id]:
            if i in self.roadDic.keys():
                temp.append(self.roadDic[i])
            else:
                temp.append(None)
        return temp

    def get_car_start_pos(self, car):
        # 通过车的信息结合图的信息得知车的初始位置
        return [0, 0]

    def get_car_end_pos(self, car):
        # 通过车的信息结合图的信息得知车的终点的位置
        return [1, 1]

    def updatexy(self):
        self.__crosses[0].xy = (0, 0)
        crosjl = {self.__crosses[0].id: 0}
        crossjl = {self.__crosses[0].id: (0, 0)}
        t = True
        while t:
            t = False
            for i in self.__crosses:
                if (i.id not in crosjl or crosjl[i.id] != 0) and i.road_id_up >= 0 and self.roadDic[
                    i.road_id_up].end == i.id and self.roadDic[i.road_id_up].start in crosjl and crosjl[
                    self.roadDic[i.road_id_up].start] == 0:
                    if i.id in crosjl:
                        if crosjl[i.id] == 2 or crosjl[i.id] == 4:
                            i.xy = (self.crossDic[self.roadDic[i.road_id_up].start].xy[0], i.xy[1])
                            crosjl[i.id] = 0
                            crossjl[i.id] = i.xy
                        elif crosjl[i.id] == 1:
                            i.xy = ((self.crossDic[self.roadDic[i.road_id_up].start].xy[0] + i.xy[0]) / 2,
                                    (self.crossDic[self.roadDic[i.road_id_up].start].xy[1] - 1 + i.xy[1]) / 2)
                    else:
                        i.xy = (self.crossDic[self.roadDic[i.road_id_up].start].xy[0],
                                self.crossDic[self.roadDic[i.road_id_up].start].xy[1] - 1)
                        crosjl[i.id] = 3
                        crossjl[i.id] = i.xy
                    t = True
                if (i.id not in crosjl or crosjl[i.id] != 0) and i.road_id_right >= 0 and self.roadDic[
                    i.road_id_right].end == i.id and self.roadDic[i.road_id_right].start in crosjl and crosjl[
                    self.roadDic[i.road_id_right].start] == 0:
                    if i.id in crosjl:
                        if crosjl[i.id] == 1 or crosjl[i.id] == 3:
                            i.xy = (i.xy[0], self.crossDic[self.roadDic[i.road_id_right].start].xy[1])
                            crossjl[i.id] = i.xy
                            crosjl[i.id] = 0
                        elif crosjl[i.id] == 2:
                            i.xy = ((self.crossDic[self.roadDic[i.road_id_right].start].xy[0] - 1 + i.xy[0]) / 2,
                                    (self.crossDic[self.roadDic[i.road_id_right].start].xy[1] + i.xy[1]) / 2)
                    else:
                        i.xy = (self.crossDic[self.roadDic[i.road_id_right].start].xy[0] - 1,
                                self.crossDic[self.roadDic[i.road_id_right].start].xy[1])
                        crosjl[i.id] = 4
                        crossjl[i.id] = i.xy
                    t = True
                if (i.id not in crosjl or crosjl[i.id] != 0) and i.road_id_down >= 0 and self.roadDic[
                    i.road_id_down].end == i.id and self.roadDic[i.road_id_down].start in crosjl and crosjl[
                    self.roadDic[i.road_id_down].start] == 0:
                    if i.id in crosjl:
                        if crosjl[i.id] == 1 or crosjl[i.id] == 3:
                            i.xy = (self.crossDic[self.roadDic[i.road_id_down].start].xy[0], i.xy[1])
                            crosjl[i.id] = 0
                            crossjl[i.id] = i.xy
                        elif crosjl[i.id] == 3:
                            i.xy = ((self.crossDic[self.roadDic[i.road_id_down].start].xy[0] + i.xy[0]) / 2,
                                    (self.crossDic[self.roadDic[i.road_id_down].start].xy[1] + 1 + i.xy[1]) / 2)
                    else:
                        i.xy = (self.crossDic[self.roadDic[i.road_id_down].start].xy[0],
                                self.crossDic[self.roadDic[i.road_id_down].start].xy[1] + 1)
                        crosjl[i.id] = 1
                        crossjl[i.id] = i.xy
                    t = True
                if (i.id not in crosjl or crosjl[i.id] != 0) and i.road_id_left >= 0 and self.roadDic[
                    i.road_id_left].end == i.id and self.roadDic[i.road_id_left].start in crosjl and crosjl[
                    self.roadDic[i.road_id_left].start] == 0:
                    if i.id in crosjl:
                        if crosjl[i.id] == 2 or crosjl[i.id] == 4:
                            i.xy = (self.crossDic[self.roadDic[i.road_id_left].start].xy[0], i.xy[1])
                            crosjl[i.id] = 0
                            crossjl[i.id] = i.xy
                        elif crosjl[i.id] == 4:
                            i.xy = ((self.crossDic[self.roadDic[i.road_id_left].start].xy[0] + 1 + i.xy[0]) / 2,
                                    (self.crossDic[self.roadDic[i.road_id_left].start].xy[1] + i.xy[1]) / 2)
                    else:
                        i.xy = (self.crossDic[self.roadDic[i.road_id_left].start].xy[0] + 1,
                                self.crossDic[self.roadDic[i.road_id_left].start].xy[1])
                        crosjl[i.id] = 2
                        crossjl[i.id] = i.xy
                    t = True
            for i in crosjl.items():
                crosjl[i[0]] = 0
        return crossjl
    # def init(self, road_path, cross_path):
    #     # road_path = u'../road.txt'
    #     # cross_path = u'../cross.txt'
    #     cross = read_txt.read_txt(cross_path)
    #     road = read_txt.read_txt(road_path)
    #     for i in road:
    #         temp = Road(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
    #         self.set_road(temp)
    #     for i in cross:
    #         temp = Cross(i[0], i[1], i[2], i[3], i[4])
    #         self.set_cross(temp)

# if __name__ == '__main__':
#     g = Graph()
#     from cross import Cross
#     from road import Road
#     import read_txt
#     g.init('../road.txt','../cross.txt')
#     print (g.updatexy())
#     print (g.crosses(0))
#     # temp = Cross(4, 5003, 5010, 5002, -1)
#     # road = Road(5003, 20, 4, 2, 4, 5, 1)
#     # g.set_cross(temp)
#     # g.set_road(road)
#     # print(g.get_roads(temp))
#     # print(g.get_road())
#     # print(g.get_cross())
#     # print(g.get_roads(temp))
