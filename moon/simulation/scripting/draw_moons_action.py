from constants import *
from simulation.scripting.action import Action


class DrawMoonsAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        moons = cast.get_actors(MOON_GROUP)
        
        for moon in moons:
            body = moon.get_body()
            radius = moon.get_radius()

            if moon.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                
            animation = moon.get_animation()
            image = animation.next_image()
            image.set_scale(radius/MOON_RADIUS)
            position = body.get_position()
            self._video_service.draw_image(image, position)