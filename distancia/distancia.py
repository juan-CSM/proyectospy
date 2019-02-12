#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def restav(p1,p2):
    distancia =  np.array([p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]])
    return distancia

def sumav(p1,p2):
    vectorsuma = np.array([p2[0] + p1[0], p2[1] + p1[1], p2[2] + p1[2]])
    return vectorsuma

def dista(p1,p2):
    distancia =  ((p1[0]-p2[0])**(2)+(p1[1]-p2[1])**(2)+(p1[2]-p2[2])**(2))**(1/2)
    return distancia

def espmedio(a,b,c):
    tofsiespm = (dista(a,c) + dista(b,c) == dista(a,b))
    return tofsiespm

def genmat(a,b):
    matrizvec = np.array([[a[0],b[0]], [a[1],b[1]]])
    return matrizvec


def findpm(a,b,c):
    if(espmedio(a,b,c)):
        pm = c
    else:
        ac = restav(a,c)
        bc = restav(b,c)
        ab = restav(a,b)
        cp = a - bc
        cpc = restav(cp,c)
        ld = restav(a,c)[0:2]
        li = genmat(ab,cpc)
        pq = np.linalg.solve(li,ld)
        pm = sumav(a,ab*float(pq[1]))
    return [a,b,c,pm]
