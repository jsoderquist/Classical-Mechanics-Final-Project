from constants import *
from simulation.directing.director import Director
from simulation.directing.scene_manager import SceneManager

def main():
    director = Director(SceneManager.VIDEO_SERVICE)
    director.start_simulation()

if __name__ == "__main__":
    main()