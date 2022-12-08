from constants import *
from simulation.scripting.action import Action


class DrawEarthAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        earth = cast.get_first_actor(EARTH_GROUP)
        body = earth.get_body(cast)

        if earth.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = earth.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)