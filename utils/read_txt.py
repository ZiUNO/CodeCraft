# -*- coding: utf-8 -*-
"""
* @Author: zhaopeng
* @Software: PyCharm
* @Time: 2019/3/27 22:15
* 读入txt
"""
def read_txt(path): # 读取txt文件，返回二维数组
    f = open(path)
    txt = f.read().split('\n')
    data = []
    for i in txt[1:]:
        data_mid = []
        for j in i[1:-1].split(','):
            data_mid.append(int(j))
        data.append(data_mid)
    return data

