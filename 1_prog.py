#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math #импортируем модуль math, базовая математическая операция
import numpy #импортируем модуль numpy
import matplotlib.pyplot as mpp # импортируем и переименовываем 


if __name__=='__main__':
    arguments = numpy.r_[0:200:0.1]# создает массив чисео от 0 до 200 с шагом 0.1
    mpp.plot(   # строит график функции
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments] # список значений функции
    )
    mpp.show() #выводит график функции
