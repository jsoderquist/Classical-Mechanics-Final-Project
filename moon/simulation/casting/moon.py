from constants import *
from simulation.casting.actor import Actor
from simulation.casting.point import Point


class Moon(Actor):
    """A solid, rectangular object that can be broken."""

    def __init__(self, body, animation, size, mass, radius, debug = False):
        """Constructs a new Moon.
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._size = size
        self._mass = mass
        self._radius = radius
        self._acceleration = Point(0,0) 
    
    def get_acceleration(self):
        """Gets the moon's acceleration.
        
        Returns:
            acceleration.
        """
        return self._acceleration
    
    def get_animation(self):
        """Gets the moon's image.
        
        Returns:
            An instance of Image.
        """
        return self._animation

    def get_body(self):
        """Gets the moon's body.
        
        Returns:
            An instance of Body.
        """
        #self._body.set_size(Point(MOON_HEIGHT*self._size.get_x(), MOON_WIDTH*self._size.get_y()))

        return self._body
    
    def get_center(self):
        """Gets the Moon's center position.
        
        Returns:
            A position point.
        """
        return self._body.get_position().add(Point(MOON_WIDTH/2,MOON_HEIGHT/2))

    def get_mass(self):
        """Gets the moon's body.
        
        Returns:
            An instance of Body.
        """
        #self._body.set_size(Point(MOON_HEIGHT*self._size.get_x(), MOON_WIDTH*self._size.get_y()))

        return self._mass

    def get_radius(self):
        """Gets the moon's radius.
        
        Returns:
            Radius.
        """
        #self._body.set_size(Point(MOON_HEIGHT*self._size.get_x(), MOON_WIDTH*self._size.get_y()))

        return self._radius

    def set_acceleration(self, acceleration):
        """Sets the moon's acceleration.
        
        """

        self._acceleration = acceleration

    def set_mass(self, mass):
        """Sets the moon's mass.
        
        """
        #self._body.set_size(Point(MOON_HEIGHT*self._size.get_x(), MOON_WIDTH*self._size.get_y()))

        self._mass = mass

    def set_radius(self, radius):
        """Sets the moon's radius.
        
        """
        #self._body.set_size(Point(MOON_HEIGHT*self._size.get_x(), MOON_WIDTH*self._size.get_y()))

        self._radius = radius