# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 20:47:54 2021

@author: Louis
"""
import math
MASS=70000000
mass=3000
G=6.67408E-11
timeFrameLength=10000 # time resolution
pos=[300,300]
POS=[200,300]
vel=[0.0005,-0.0002]



def Orbiter(pos,POS,veloc,MASS,mass):
    # finding the orbital radius
    rad=math.sqrt(((pos[0]+POS[0])**2)+((pos[1]-POS[1])**2))
    # getting the acceleration
    # acc=(G*MASS*rad)/abs(rad)**3
    acc=[(-(G*MASS)/(rad**2))*((pos[0]-POS[0])/rad),(-(G*MASS)/(rad**2))*((pos[1]-POS[1])/rad)] #(pos[i]/rad) being the unit vector
    # getting the new velocity vector
    veloc+=[acc[0]*timeFrameLength,acc[1]*timeFrameLength]
    for i in range(2):
        veloc[i]+=acc[i]*timeFrameLength 
    # veloc[0]+=(acc*timeFrameLength)*((pos[0]-POS[0])/rad) #(pos[i]/rad) being to make it go towards the object
    # veloc[1]+=(acc*timeFrameLength)*((pos[1]-POS[1])/rad) #(pox`s[i]/rad) being to make it go towards the object
    # for i in range(2):
    #     veloc[i]+=(acc*timeFrameLength)*((pos[i]+POS[i])/rad) #(pos[i]/rad) being to make it go towards the object
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
        dx=new[1][0]
        dy=new[1][1]
        planets[i] = (x, y, dx, dy, r, color)
        
    canvas.fill(pg.Color("black"))
    for x, y, dx, dy, r, color in planets:
        pg.draw.circle(canvas, color, (x, y), r)
        pg.draw.circle(canvas, "red", (POS[0], POS[1]), 30)
        
pygamebg.frame_loop(50, new_frame)



"""
To make this do a binary orbit - i just have to find the centre of the two masses right?
"""






