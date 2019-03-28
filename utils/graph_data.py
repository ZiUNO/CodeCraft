# -*- coding: utf-8 -*-
"""
* @Author: zhaopeng
* @Software: PyCharm
* @Time: 2019/3/27 22:13
* 读入道路与路口文件，将道路信息整合
* 格式为
* 道路id, 道路长度,最高速度 ,车道数目 ,连接节点id
"""
from utils.road import Road
from utils import read_txt


def graph_data(data):
    data_graph = {}
    for i in data:
        if i[4] not in data_graph.keys():
            # 道路id 0、道路长度 1、最高速度 2、车道数目 3、连接节点id 4
            data_graph[i[4]] = [i[0], i[1], i[2], i[3], i[5]]
        else:
            data_graph[i[4]].extend([i[0], i[1], i[2], i[3], i[5]])
        if i[6]:
            if i[5] not in data_graph.keys():
                data_graph[i[5]] = [i[0], i[1], i[2], i[3], i[4]]
            else:
                data_graph[i[5]].extend([i[0], i[1], i[2], i[3], i[4]])
    for key in data_graph:
        data_graph[key].append(int(len(data_graph[key]) / 5))
    return data_graph


# 功能：获取道路的方向
def cross_data(cross):
    road_direction = {}
    for i in cross:
        road_direction[i[0]] = i[1:]
    return road_direction


def update():
    Road.update()


def get_roads(cross):
    date_graph = get_graph()

    return date_graph[cross]


def get_aim_relative_pos(graph):
    return 0


def get_graph():
    road_path = u'../road.txt'

    road = read_txt.read_txt(road_path)

    data_graph = graph_data(road)

    # for key in data_graph:
    #     print(key, data_graph[key])

    return data_graph


def get_cross_direction():
    cross_path = u'../cross.txt'
    cross = read_txt.read_txt(cross_path)

    road_direction = cross_data(cross)
    return road_direction

# if __name__ == '__main__':
#     print(get_cross_direction())
