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
        self.roadDic = {}

    @property
    def graDic(self):
        return self.__graDic

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
#     from utils.cross import Cross
#     from utils.road import Road
#     temp = Cross(4, 5003, 5010, 5002, -1)
#     road = Road(5003, 20, 4, 2, 4, 5, 1)
#     g.set_cross(temp)
#     g.set_road(road)
#     print(g.get_roads(temp))
#     # print(g.get_road())
#     # print(g.get_cross())
#
#     # print(g.get_roads(temp))
