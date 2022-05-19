#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Для своего индивидуального задания лабораторной работы 2.23 необходимо
реализоватьвычисление значений в двух функций в отдельных процессах
"""

from multiprocessing import Process
from math import exp, pow, log, factorial

accuracy = 0.0000001


def func_y1(x):
    yx = (exp(x) - exp(-x)) / 2
    return yx


def func_y2(x):
    yx = 3 ** x
    return yx


def sum1(x):
    s, n, cur = 0, 1, 0
    while True:
        pre = (x ** (n + 2)) / factorial(n + 2)
        n += 2
        if abs(cur - pre) < accuracy:
            break
        cur = (x ** (n + 2)) / factorial(n + 2)
        s += cur
    return s


def sum2(x):
    s, n, cur = 0, 0, 0
    while True:
        pre = (pow(x, n) * pow(log(3), n)) / factorial(n)
        n += 1
        if abs(cur - pre) < accuracy:
            break
        cur = (pow(x, n) * pow(log(3), n)) / factorial(n)
        s += cur
    return s


def compare(first, second, x):
    res = first(x) - second(x)
    print(f"Результат: {res}")


if __name__ == '__main__':
    proc1 = Process(target=compare(sum1, func_y1, 1))
    proc2 = Process(target=compare(sum2, func_y2, 2))
    proc1.start()
    proc2.start()
    proc1.join()
    proc2.join()
