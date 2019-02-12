#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = np.array([0,0,0])
b = np.array([2,0,0])
c = np.array([1,1,0])

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
        print(pm)
    return [a,b,c,pm]

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
'''
partx = np.array([a[0],b[0],c[0],pm[0]])
party = np.array([a[1],b[1],c[1],pm[1]])
partz = np.array([a[2],b[2],c[2],pm[2]])
'''
puntos = findpm(a,b,c)
for i in puntos:
    ax.scatter(i[0],i[1],i[2])

plt.show()
