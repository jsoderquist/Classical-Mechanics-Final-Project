from constants import *
from simulation.casting.actor import Actor
from simulation.casting.point import Point


class Earth(Actor):
    """An object representing the Earth."""
    
    def __init__(self, body, animation, debug = False):
        """Constructs a new Earth.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._hit_earth = 0
        self._escaped_orbit = 0
        self._largest_debris = 0

    def add_to_hit_earth(self, mass):
        """Adds mass to the amount that's hit Earth.
        
        """

        self._hit_earth += mass

    def add_to_escaped_orbit(self, mass):
        """Adds mass to the amount that's escaped the orbit of Earth.
        
        """

        self._escaped_orbit += mass
    
    def get_animation(self):
        """Gets the bat's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self, cast):
        """Gets the bat's body.
        
        Returns:
            An instance of Body.
        """
        return self._body
        
    def get_center(self):
        """Gets the Earth's center position.
        
        Returns:
            A position point.
        """
        return self._body.get_position().add(Point(EARTH_INIT_WIDTH/2,EARTH_INIT_HEIGHT/2))

    def get_escaped_orbit(self):
        """Gets the amount of mass that escapes the orbit of the Earth.
        
        Returns:
            A mass variable.
        """

        return self._escaped_orbit

    def get_hit_earth(self):
        """Gets the amount of mass that hit the Earth.
        
        Returns:
            A mass variable.
        """

        return self._hit_earth

    def get_largest_debris(self):
        """Gets the largest mass that hit the Earth.
        
        Returns:
            A mass variable.
        """

        return self._largest_debris

    def move_next(self):
        """Moves the bat using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def set_largest_debris(self, debris):
        """Sets the largest mass that hit the Earth.
        
        """

        self._largest_debris = debris