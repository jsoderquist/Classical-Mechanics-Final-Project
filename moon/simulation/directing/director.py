from constants import *
from simulation.casting.cast import Cast
from simulation.directing.scene_manager import SceneManager
from simulation.scripting.action_callback import ActionCallback
from simulation.scripting.script import Script


class Director(ActionCallback):
    """A person who directs the simulation."""

    def __init__(self, video_service):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
        self._cast = Cast()
        self._script = Script()
        self._scene_manager = SceneManager()
        
    def start_simulation(self):
        """Starts the simulation. Runs the main simulation loop."""
        self._scene_manager.prepare_scene(self._cast, self._script)
        self._execute_actions(INITIALIZE)
        self._execute_actions(LOAD)
        while self._video_service.is_window_open():
            self._execute_actions(INPUT)
            self._execute_actions(UPDATE)
            self._execute_actions(OUTPUT)
        self._execute_actions(UNLOAD)
        self._execute_actions(RELEASE)
        #display amount of mass went where
        earth = self._cast.get_first_actor(EARTH_GROUP)
        hit_earth = earth.get_hit_earth()
        escaped = earth.get_escaped_orbit()
        orbiting = MOON_MASS - escaped - hit_earth
        largest_debris  = earth.get_largest_debris()
        print(hit_earth,"kg hit Earth")
        print(escaped,"kg flew out of orbit")
        print(orbiting,"kg were still in orbit at the end of the simulation")
        print(hit_earth / MOON_MASS * 100,"% hit Earth")
        print(escaped / MOON_MASS * 100,"% flew out of orbit")
        print(orbiting / MOON_MASS * 100,"% was still in orbit at the end of the simulation")
        print("The largest piece of debris that hit Earth was",largest_debris,"kg")
        
    def _execute_actions(self, group):
        """Calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = self._script.get_actions(group)    
        for action in actions:
            action.execute(self._cast, self._script, self)          