# -*- coding: utf-8 -*-
"""
* @Author: ziuno
* @Software: PyCharm
* @Time: 2019/3/27 20:39
"""


class Graph(object):
    graDic = {}

    def __init__(self):
        self.__roads = []
        self.__crosses = []

    def set_road(self, road):
        self.__roads.append(road)

    def set_cross(self, cross):
        self.__crosses.append(cross)

        self.graDic[cross.id] = [cross.road_id_up, cross.road_id_right, cross.road_id_down, cross.road_id_left]

    def get_cross(self):
        return self.__crosses

    def get_road(self):
        return self.__roads

    def update(self):
        for i in self.get_road():
            i.update()

    def get_roads(self, cross):
        return self.graDic[cross]

    def get_aim_relative_pos(self, graph):
        return 0

    # def init(self, road_path, cross_path):
    #     # road_path = u'../road.txt'
    #     # cross_path = u'../cross.txt'
    #     cross = read_txt.read_txt(cross_path)
    #     road = read_txt.read_txt(road_path)
    #     for i in road:
    #         temp = Road(i[0], i[1], i[2], i[3], i[4], i[5], [6])
    #         self.set_road(temp)
    #     for i in cross:
    #         temp = Cross(i[0], i[1], [2], i[3], i[4])
    #         self.set_cross(temp)

# if __name__ == '__main__':
#     g = Graph()
#     g.init("../road.txt", "../cross.txt")
#     for i in g.get_road():
#
#         print(i.id)
#     for i in g.get_cross():
#         print(i)
