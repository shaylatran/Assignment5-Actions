from math import pi
from datetime import date


def firstrun():
    return "success"


def areaofCircle(radius):
    return (pi*radius*radius)


def firstandlastofList(list):
    return [list[0], list[-1]]


def numberofDays(date1, date2):
    num = date2 - date1
    return num
