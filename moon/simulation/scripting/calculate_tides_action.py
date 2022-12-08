from constants import *
from simulation.casting.point import Point
from simulation.scripting.action import Action
from simulation.scripting.rip_moon_action import RipMoonAction
from math import atan,sqrt,sin,cos

class CalculateTidesAction(Action):
    """Calculation of tides on the moon
    
    
    """

    def execute(self, cast, script, callback):
        """Calculates tides on the moon

        Args:
            cast: An instance of Cast containing the actors in the simulation.
            script: An instance of Script containing the actions in the simulation.
            callback: An instance of ActionCallback so we can change the scene.
        """
        RIP_MOON_ACTION = RipMoonAction()
        moons = cast.get_actors(MOON_GROUP)
        earth = cast.get_first_actor(EARTH_GROUP)
        earth_position = earth.get_center()
        x_earth = earth_position.get_x()/SCALE
        y_earth = earth_position.get_y()/SCALE
        #print(len(moons))

        for moon in moons:
            body = moon.get_body()
            position = moon.get_center()
            body_position = body.get_position()
            velocity = body.get_velocity()
            velocity_mag = sqrt(velocity.get_x()**2+velocity.get_y()**2)
            x_moon = position.get_x()/SCALE
            y_moon = position.get_y()/SCALE
            moon_mass = moon.get_mass()
            moon_radius = moon.get_radius()
            
            r = sqrt((x_moon-x_earth)**2+(y_moon-y_earth)**2)

            a_tidal = G*EARTH_MASS * (1/(r - moon_radius)**2 - 1/(r + moon_radius)**2)
            a_moon_gravity = G*moon_mass/moon_radius**2
            #print(a_tidal,a_moon_gravity)

            #get rid of the moon if it hit the earth
            if r < (EARTH_RADIUS + moon_radius): 
                earth.add_to_hit_earth(moon_mass)
                cast.remove_actor(MOON_GROUP,moon)
                largest_debris = earth.get_largest_debris()
                if moon_mass > largest_debris:
                    earth.set_largest_debris(moon_mass)
            elif (r > 2*MOON_RA and velocity_mag > sqrt(2*G*EARTH_MASS/r)): #get rid of the moon if it's far away and past escape velocity
                earth.add_to_escaped_orbit(moon_mass)
                cast.remove_actor(MOON_GROUP,moon)
            elif a_tidal > a_moon_gravity and len(moons)<50:
                angle = atan(-(y_moon-y_earth)/(x_moon-x_earth))
                
                moon.set_mass(moon_mass/2)
                new_radius = moon_radius/2**(1/3)
                #radius_difference = moon_radius - new_radius
                d = 3*moon_radius/8 #center of mass of a hemisphere is the distance to move to not lose energy
                moon.set_radius(new_radius)
                body.set_size(new_radius/MOON_RADIUS)
                body.set_position(body_position.add(Point(-d*cos(angle)*SCALE,d*sin(angle)*SCALE)))
                #body.set_position(body_position.add(Point(-moon_radius/2*cos(angle)*SCALE,moon_radius/2*sin(angle)*SCALE)))
                #body.set_position(body_position.add(Point(-radius_difference*cos(angle)*SCALE,radius_difference*sin(angle)*SCALE)))
                RIP_MOON_ACTION.execute(cast,script,callback,angle,moon_mass,moon_radius,body_position,velocity)
                #body.set_position(Point(x_moon+moon_radius/2,y_moon)) #This is just a test line
