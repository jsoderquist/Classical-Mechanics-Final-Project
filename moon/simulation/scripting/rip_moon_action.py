from constants import *
from simulation.casting.animation import Animation
from simulation.casting.body import Body
from simulation.casting.moon import Moon
from simulation.casting.point import Point
from simulation.scripting.action import Action
from math import sin, cos
from random import randint


class RipMoonAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback, angle, mass, radius,position,velocity):
        
        #print(angle)
        #position = Point(x, y)
        size = Point(MOON_WIDTH, MOON_HEIGHT) #scale these when I scale the image
        #velocity = Point(0,0)
        images = MOON_IMAGES

        new_radius = radius/2**(1/3)
        radius_difference = radius-new_radius
        d = 3*radius/8 #center of mass of a hemisphere is the distance to move to not lose energy
        position = position.add(Point(d*cos(angle)*SCALE,-d*sin(angle)*SCALE))
        #position = position.add(Point(radius/2*cos(angle)*SCALE,-radius/2*sin(angle)*SCALE))
        #position = position.add(Point(radius_difference*cos(angle)*SCALE,-radius_difference*sin(angle)*SCALE))

        size = Point(MOON_WIDTH*new_radius/MOON_RADIUS, MOON_HEIGHT*new_radius/MOON_RADIUS)

        body = Body(position, size, velocity)
        animation = Animation(images, MOON_RATE, MOON_DELAY)

        moon = Moon(body, animation, size, mass/2, radius/2**(1/3))
        cast.add_actor(MOON_GROUP, moon)