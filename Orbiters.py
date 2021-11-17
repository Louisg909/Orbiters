# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 20:47:54 2021

@author: Louis
"""
import math
MASS=4000000
mass=3000
G=6.67408E-11
timeFrameLength=10000 # time resolution
pos=[200,300]
POS=[200,200]
vel=[0.000521944364,-0]



def Orbiter(pos,POS,veloc,MASS,mass):
    # finding the orbital radius
    rad=math.sqrt((POS[0]-pos[0])**2+(POS[1]-pos[1])**2)
    # getting the acceleration
    # acc=(G*MASS*rad)/abs(rad)**3
    acc=(G*MASS)/abs(rad)**2
    # getting the new velocity vector
    for i in range(2):
        veloc[i]+=(acc*timeFrameLength)*((POS[i]-pos[i])/rad) #(pos[i]/rad) being to make it go towards the object
    # getting the new position
    for i in range(2):
        pos[i]+=veloc[i]*timeFrameLength
    return [pos,veloc]



import pygame as pg
import pygamebg
# initialise position and velocity
(width, height) = (700, 400)
canvas = pygamebg.open_window(width, height, "Orbiter")
planets = [(pos[0],pos[1],vel[0],vel[1],10,"blue")]

def new_frame():
    for i in range(1):
        x, y, dx, dy, r, color = planets[i]
        new=Orbiter([x,y],POS,[dx,dy],MASS,mass)
        x=new[0][0]
        y= new[0][1]
        planets[i] = (x, y, dx, dy, r, color)
        
    canvas.fill(pg.Color("darkgray"))
    for x, y, dx, dy, r, color in planets:
        pg.draw.circle(canvas, color, (x, y), r)
        pg.draw.circle(canvas, "red", (POS[0], POS[1]), 30)
        
pygamebg.frame_loop(50, new_frame)



"""
To make this do a binary orbit - i just have to find the centre of the two masses right?
"""






