from constants import *
from simulation.casting.point import Point
from simulation.scripting.action import Action


class MoveEarthAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        earth = cast.get_first_actor(EARTH_GROUP)
        body = earth.get_body(cast)
        velocity = body.get_velocity()
        vx = velocity.get_x()
        vy = velocity.get_y()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        earth_position = earth.get_center()
        x_earth = earth_position.get_x()/SCALE
        y_earth = earth_position.get_y()/SCALE
        #print(x_earth,y_earth)
        
        moons = cast.get_actors(MOON_GROUP)
        dt = DT

        ax = 0
        ay = 0
        
        for i in range(ITERATIONS):
            
            #'''
            for debris in moons:
                debris_position = debris.get_center()
                x_debris = debris_position.get_x()/SCALE
                y_debris = debris_position.get_y()/SCALE
                debris_mass = debris.get_mass()

                ax += -G*debris_mass/((x_earth-x_debris)**2+(y_earth-y_debris)**2)**(1.5)*(x_earth-x_debris)
                ay += -G*debris_mass/((x_earth-x_debris)**2+(y_earth-y_debris)**2)**(1.5)*(y_earth-y_debris)
            #'''
            vx=vx+ax*dt
            vy=vy+ay*dt
            #print(vy,vx)

            x_earth += vx*dt
            y_earth += vy*dt
        
        position = Point((x_earth)*SCALE - EARTH_INIT_WIDTH/2,(y_earth)*SCALE - EARTH_INIT_HEIGHT/2)
        velocity = Point(vx,vy)
        #print((x_earth)*SCALE - EARTH_INIT_WIDTH/2-CENTER_X,(y_earth)*SCALE - EARTH_INIT_HEIGHT/2-CENTER_Y)
        
        body.set_position(position)
        body.set_velocity(velocity)
        