from constants import *
from simulation.casting.point import Point
from simulation.scripting.action import Action


class MoveMoonAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        moons = cast.get_actors(MOON_GROUP)
        dt = DT
        for i in range(ITERATIONS):
            #calculate acceleration of moons
            for moon in moons:
                body = moon.get_body()
                position = moon.get_center()
                x_moon = position.get_x()/SCALE
                y_moon = position.get_y()/SCALE

                earth = cast.get_first_actor(EARTH_GROUP)
                earth_position = earth.get_center()
                x_earth = earth_position.get_x()/SCALE
                y_earth = earth_position.get_y()/SCALE

                velocity = body.get_velocity()
                vx = velocity.get_x()
                vy = velocity.get_y()
                ax = 0
                ay = 0
                
                #for i in range(ITERATIONS):
                ax=-G*EARTH_MASS/((x_moon-x_earth)**2+(y_moon-y_earth)**2)**(1.5)*(x_moon-x_earth) #r on the bottom is cubed because x/r is the cos(theta)
                ay=-G*EARTH_MASS/((x_moon-x_earth)**2+(y_moon-y_earth)**2)**(1.5)*(y_moon-y_earth) #interaction with the sun
                
                #'''
                for debris in moons:
                    if not (debris == moon):
                        debris_position = debris.get_center()
                        x_debris = debris_position.get_x()/SCALE
                        y_debris = debris_position.get_y()/SCALE
                        debris_mass = debris.get_mass()

                        ax += -G*debris_mass/((x_moon-x_debris)**2+(y_moon-y_debris)**2)**(1.5)*(x_moon-x_debris)
                        ay += -G*debris_mass/((x_moon-x_debris)**2+(y_moon-y_debris)**2)**(1.5)*(y_moon-y_debris)
                #'''

                moon.set_acceleration(Point(ax,ay))
                '''
                    vx=vx+ax*dt
                    vy=vy+ay*dt

                    x_moon += vx*dt
                    y_moon += vy*dt
                
                position = Point((x_moon)*SCALE - MOON_WIDTH/2,(y_moon)*SCALE - MOON_HEIGHT/2)
                velocity = Point(vx,vy)
                
                body.set_position(position)
                body.set_velocity(velocity)
                '''
                #move the moons
                for moon in moons:
                    body = moon.get_body()
                    position = moon.get_center()
                    x_moon = position.get_x()/SCALE
                    y_moon = position.get_y()/SCALE
                    velocity = body.get_velocity()
                    vx = velocity.get_x()
                    vy = velocity.get_y()
                    acceleration = moon.get_acceleration()
                    ax = acceleration.get_x()
                    ay = acceleration.get_y()

                    vx=vx+ax*dt
                    vy=vy+ay*dt

                    x_moon += vx*dt
                    y_moon += vy*dt
                    
                    position = Point((x_moon)*SCALE - MOON_WIDTH/2,(y_moon)*SCALE - MOON_HEIGHT/2)
                    velocity = Point(vx,vy)
                    
                    body.set_position(position)
                    body.set_velocity(velocity)