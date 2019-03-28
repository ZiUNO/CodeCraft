# -*- coding: utf-8 -*-
"""
* @Author: ziuno
* @Software: PyCharm
* @Time: 2019/3/27 21:05
"""

class Car(object):
    def __init__(self, id, start, end, speed, plan_time):
        self.__id = id
        self.__start = start
        self.__end = end
        self.__speed = speed
        self.__plan_time = plan_time
        self.cur_pos = start

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
def getCarList():

    import read_txt
    myCarList = []

    car_path = u'../car.txt'
    mycar = read_txt.read_txt(car_path)
    for i in mycar:
        temp = Car(i[0],i[1],i[2],i[3],i[4])
        myCarList.append(temp)


    return myCarList



