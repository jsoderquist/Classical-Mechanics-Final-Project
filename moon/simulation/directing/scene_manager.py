from constants import *
from simulation.casting.animation import Animation
from simulation.casting.body import Body
from simulation.casting.moon import Moon
from simulation.casting.point import Point
from simulation.casting.earth import Earth
from simulation.scripting.calculate_tides_action import CalculateTidesAction
from simulation.scripting.collisions_action import CollisionsAction
from simulation.scripting.draw_moons_action import DrawMoonsAction
from simulation.scripting.draw_earth_action import DrawEarthAction
from simulation.scripting.end_drawing_action import EndDrawingAction
from simulation.scripting.initialize_devices_action import InitializeDevicesAction
from simulation.scripting.load_assets_action import LoadAssetsAction
from simulation.services.raylib.raylib_mouse_service import RaylibMouseService
from simulation.scripting.move_moon_action import MoveMoonAction
from simulation.scripting.move_earth_action import MoveEarthAction
from simulation.scripting.release_devices_action import ReleaseDevicesAction
from simulation.scripting.rip_moon_action import RipMoonAction
from simulation.scripting.start_drawing_action import StartDrawingAction
from simulation.scripting.unload_assets_action import UnloadAssetsAction
from simulation.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from simulation.services.raylib.raylib_physics_service import RaylibPhysicsService
from simulation.services.raylib.raylib_video_service import RaylibVideoService
from random import randint


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    #AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    MOUSE_SERVICE = RaylibMouseService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(SIMULATION_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    CALCULATE_TIDES_ACTION = CalculateTidesAction()
    COLLISIONS_ACTION = CollisionsAction()
    DRAW_MOONS_ACTION = DrawMoonsAction(VIDEO_SERVICE)
    DRAW_EARTH_ACTION= DrawEarthAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(VIDEO_SERVICE)
    MOVE_MOON_ACTION = MoveMoonAction()
    MOVE_EARTH_ACTION = MoveEarthAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, cast, script):
        self._prepare_new_simulation(cast, script)

    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_simulation(self, cast, script):
        cast.clear_actors(MOON_GROUP)
        self._add_moon(cast)
        self._add_earth(cast)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        self._add_update_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------

    def _add_moon(self, cast):
        #x = CENTER_X - MOON_WIDTH / 2 + (MOON_RP*SCALE) #moon at perigee
        x = CENTER_X - MOON_WIDTH / 2 - (MOON_RA*SCALE) #moon at apogee
        y = CENTER_Y - MOON_HEIGHT / 2
        
        position = Point(x, y)
        size = Point(MOON_WIDTH, MOON_HEIGHT)
        #velocity = Point(0, -MOON_VP) #moon at perigee
        velocity = Point(0, MOON_VA) #moon at perigee
        images = MOON_IMAGES

        body = Body(position, size, velocity)
        animation = Animation(images, MOON_RATE, MOON_DELAY)

        moon = Moon(body, animation, size, MOON_MASS, MOON_RADIUS)
        cast.add_actor(MOON_GROUP, moon)

    def _add_earth(self, cast):
        cast.clear_actors(EARTH_GROUP)
        x = CENTER_X - EARTH_INIT_WIDTH / 2
        y = CENTER_Y - EARTH_INIT_HEIGHT / 2
        position = Point(x, y)
        size = Point(EARTH_INIT_WIDTH, EARTH_INIT_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(EARTH_IMAGES, EARTH_RATE)
        earth = Earth(body, animation)
        cast.add_actor(EARTH_GROUP, earth)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_MOONS_ACTION)
        script.add_action(OUTPUT, self.DRAW_EARTH_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        #script.add_action(UPDATE, self.MOVE_EARTH_ACTION)
        script.add_action(UPDATE, self.MOVE_MOON_ACTION)
        script.add_action(UPDATE, self.CALCULATE_TIDES_ACTION)
        #script.add_action(UPDATE, self.COLLISIONS_ACTION)