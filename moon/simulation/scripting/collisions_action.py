from constants import *
from simulation.casting.point import Point
from simulation.scripting.action import Action
from simulation.casting.animation import Animation
from simulation.casting.body import Body
from simulation.casting.moon import Moon
from simulation.scripting.rip_moon_action import RipMoonAction
from math import atan,sqrt,sin,cos

class CollisionsAction(Action):
    """Calculation of collisions. Combines debris
    
    
    """

    def execute(self, cast, script, callback):
        """Calculates what happens in collisions

        Args:
            cast: An instance of Cast containing the actors in the simulation.
            script: An instance of Script containing the actions in the simulation.
            callback: An instance of ActionCallback so we can change the scene.
        """
        moons = cast.get_actors(MOON_GROUP)

        deleted = []

        for moon in moons:
            if not (moon in deleted):
                body = moon.get_body()
                position = moon.get_center()
                x_moon = position.get_x()/SCALE
                y_moon = position.get_y()/SCALE
                radius = moon.get_radius()
                mass = moon.get_mass()

                velocity = body.get_velocity()
                vx = velocity.get_x()
                vy = velocity.get_y()
                    
                #'''
                for debris in moons:
                    if not (debris == moon or (debris in deleted)):
                        debris_position = debris.get_center()
                        x_debris = debris_position.get_x()/SCALE
                        y_debris = debris_position.get_y()/SCALE
                        debris_mass = debris.get_mass()
                        debris_radius = debris.get_radius()
                        r = sqrt((x_moon-x_debris)**2+(y_moon-y_debris)**2)

                        #print(r, radius + debris_radius)

                        if r < radius + debris_radius:
                            #find center of mass
                            combined_mass = debris_mass + mass
                            combined_radius = (3*combined_mass/4/MOON_DENSITY/pi)**(1/3)
                            x_COM = (debris_mass*x_debris + mass*x_moon) / combined_mass
                            y_COM = (debris_mass*y_debris + mass*y_moon) / combined_mass

                            #get Earth position
                            earth = cast.get_first_actor(EARTH_GROUP)
                            earth_position = earth.get_center()
                            x_earth = earth_position.get_x()/SCALE
                            y_earth = earth_position.get_y()/SCALE

                            #calculate tides to see if we need to combine
                            dist = sqrt((x_COM-x_earth)**2+(y_COM-y_earth)**2)

                            a_tidal = G*EARTH_MASS * (1/(dist - combined_radius)**2 - 1/(dist + combined_radius)**2)
                            a_moon_gravity = G*combined_mass/combined_radius**2
                            
                            #'''
                            #split if it seems they haven't just split
                            if a_tidal < a_moon_gravity:# or abs(debris_mass - mass) > 0.1:
                                #calculate velocity
                                debris_body = debris.get_body()
                                debris_velocity = debris_body.get_velocity()
                                debris_vx = debris_velocity.get_x()
                                debris_vy = debris_velocity.get_y()
                                combined_vx = (mass*vx + debris_mass*debris_vx) / combined_mass
                                combined_vy = (mass*vy + debris_mass*debris_vy) / combined_mass
                                
                                #add combined moon
                                new_position = Point(x_COM, y_COM)
                                size = Point(MOON_WIDTH*combined_radius/MOON_RADIUS, MOON_HEIGHT*combined_radius/MOON_RADIUS)
                                combined_velocity = Point(combined_vx, combined_vy)
                                images = MOON_IMAGES

                                new_body = Body(new_position, size, combined_velocity)
                                animation = Animation(images, MOON_RATE, MOON_DELAY)

                                new_moon = Moon(new_body, animation, size, combined_mass, combined_radius)
                                cast.add_actor(MOON_GROUP, new_moon)

                                #delete pieces
                                #print(debris, moon)
                                #print(moons)
                                print(moon,debris,"here")
                                deleted.append(debris)
                                deleted.append(moon)
                                cast.remove_actor(MOON_GROUP,debris)
                                cast.remove_actor(MOON_GROUP,moon)
                                
                            #'''

                            '''
                            #calculate velocity
                            debris_body = debris.get_body()
                            debris_velocity = debris_body.get_velocity()
                            debris_vx = debris_velocity.get_x()
                            debris_vy = debris_velocity.get_y()
                            combined_vx = (mass*vx + debris_mass*debris_vx) / combined_mass
                            combined_vy = (mass*vy + debris_mass*debris_vy) / combined_mass
                            
                            #add combined moon
                            new_position = Point(x_COM, y_COM)
                            size = Point(MOON_WIDTH*combined_radius/MOON_RADIUS, MOON_HEIGHT*combined_radius/MOON_RADIUS)
                            combined_velocity = Point(combined_vx, combined_vy)
                            images = MOON_IMAGES

                            new_body = Body(new_position, size, combined_velocity)
                            animation = Animation(images, MOON_RATE, MOON_DELAY)

                            moon = Moon(new_body, animation, size, combined_mass, combined_radius)
                            cast.add_actor(MOON_GROUP, moon)

                            #delete pieces
                            cast.remove_actor(MOON_GROUP,moon)
                            cast.remove_actor(MOON_GROUP,debris)
                            '''
            #'''