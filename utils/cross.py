# -*- coding: utf-8 -*-
"""
* @Author: jinzhe
* @Software: PyCharm
* @Time: 2019/3/27 21:04
"""
def move(data):
    data
import read_txt
import graph_data
road_path = u'../road.txt'
cross_path = u'../cross.txt'
road = read_txt.read_txt(road_path)
cross = read_txt.read_txt(cross_path)
road_direction = graph_data.cross_data(cross)
data_graph=graph_data.graph_data(road)
print (data_graph)