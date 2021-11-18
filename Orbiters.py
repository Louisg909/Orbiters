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
vel=[0.000,-0.0004]
pos2=[400,300]
vel2=[0,0.0004]
mass2=3000



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
planets = [(pos[0],pos[1],vel[0],vel[1],10,"blue"),(pos2[0],pos2[1],vel2[0],vel2[1],10,"green")]

def new_frame():
    for i in range(2):
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

#%%


import math
MASS=70000000
mass=3000
G=6.67408E-11
timeFrameLength=10000 # time resolution
pos=[200,300]
POS=[200,300]
vel=[0.000,-0.0004]
VEL=[0,0]



def Orbiter(pos,POS,veloc,MASS,mass):
    """
    Find the new position and velocity of an Orbiter

    Parameters
    ----------
    pos : list
        Position vector of the orbiter.
    POS : list
        Position vector of the centre object.
    veloc : list
        Velocity of the orbiter.
    MASS : int
        Mass of the centre object.
    mass : int
        Mass of the orbiter.

    Returns
    -------
    list
        Returns a list of two vectors, first being the new position vector and the second being the new velocity vector.

    """
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
planets = [(pos[0],pos[1],vel[0],vel[1],10,"blue"),(POS[0],POS[1],VEL[0],VEL[1],30,"red")]

def new_frame():
    # for i in range(2):
    #     x, y, dx, dy, r, color = planets[i]
    #     new=Orbiter([x,y],POS,[dx,dy],MASS,mass)
    #     x=new[0][0]
    #     y= new[0][1]
    #     dx=new[1][0]
    #     dy=new[1][1]
    #     planets[i] = (x, y, dx, dy, r, color)
    x, y, dx, dy, r, color = planets[0]
    new=Orbiter([planets[0][0],planets[0][1]],[planets[1][0],planets[1][1]],[dx,dy],MASS,mass)
    x=new[0][0]
    y= new[0][1]
    dx=new[1][0]
    dy=new[1][1]
    planets[0] = (x, y, dx, dy, r, color)
    x, y, dx, dy, r, color = planets[1]
    new=Orbiter([planets[1][0],planets[1][1]],[planets[0][0],planets[0][1]],[dx,dy],MASS,mass)
    x=new[0][0]
    y= new[0][1]
    dx=new[1][0]
    dy=new[1][1]
    planets[1] = (x, y, dx, dy, r, color)
    
        
    canvas.fill(pg.Color("black"))
    for x, y, dx, dy, r, color in planets:
        pg.draw.circle(canvas, color, (x, y), r)
        # pg.draw.circle(canvas, "red", (POS[0], POS[1]), 30)
        
pygamebg.frame_loop(50, new_frame)




#%%

import random.randint as rand

G=6.67408E-11
timeFrameLength=10000 # time resolution
POS=[200,300]
MASS=70000000
NOplanets=5
planets=[[]]

class Planet():
    def __init__(self):
        """
        Initialising orbiter object

        Parameters
        ----------
        mass : int
            Mass of orbiter.
        pos : list
            Initial position of orbiter.
        vel : list
            Initial velocity of orbiter.

        """
        self.mass=rand(100,7000)
        self.pos=[rand(0,700),rand(0,400)]
        self.vel=[rand(-0.005,0.005),rand(-0.005,0.005)]
        

for n in range(NOplanets):
    planets.append(Planet())








