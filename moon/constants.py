from simulation.casting.color import Color
from math import sqrt,pi

# -------------------------------------------------------------------------------------------------- 
# GENERAL SIMULATION CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# SIMULATION
SIMULATION_NAME = "Moon Orbit"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 980
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)
BLUE = Color(0, 0, 100)

# KEYS
LEFT = "a"
RIGHT = "d"
DOWN = "s"
UP = "w"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"
LEFT_CLICK = "left"

# SCENES
NEW_SIMULATION = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
SIMULATION_OVER = 4

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

'''
# BUBBLE
BUBBLE_GROUP = "bubbles"
BUBBLE_IMAGE = "moon/assets/images/102.png"
BUBBLE_WIDTH = 10
BUBBLE_HEIGHT = 10
BUBBLE_VELOCITY = 8
'''

#SCALE = 800*10**-9
SCALE = 15.67*10**-6
G=6.673E-11

# EARTH
EARTH_GROUP = "earths"
EARTH_IMAGES = ["moon/assets/images/100.png"]
EARTH_INIT_WIDTH = 200
EARTH_INIT_HEIGHT = 200
EARTH_RATE = 6
#EARTH_VELOCITY = 4
EARTH_MASS=5.97219E24   # mass of the earth
EARTH_RADIUS=6.3781E6    # radius of the earth

# MOON
MOON_GROUP = "moons"
MOON_IMAGES = ["moon/assets/images/002.png"]
MOON_WIDTH = 54
MOON_HEIGHT = 54
MOON_DELAY = 0.5
MOON_RATE = 4
MOON_MASS = 7.3476*10**22
MOON_RADIUS = 1.7374*10**6
HP = 5.3*10**6
HA = 1*10**7
#HA = 0.3633*10**9 - EARTH_RADIUS #pull in from moon's actual closest distance away
#MOON_RP=  0.3633*10**9 #distance from Earth at perigee
#MOON_RA=  0.4055*10**9 #distance from Earth at apogee
#MOON_RP=  0.81358*10**7 #within Roche limit
#MOON_RA = MOON_RP #pull moon in from it's closest position in real orbit
MOON_RP =  HP + EARTH_RADIUS
#MOON_RP=  1.22*10**7 #outside Roche limit
MOON_RA =  HA + EARTH_RADIUS
MOON_VP=sqrt(2*G*(EARTH_MASS+MOON_MASS)*MOON_RA/((MOON_RA+MOON_RP)*MOON_RP))  # speed at perigee
MOON_VA=sqrt(2*G*(EARTH_MASS+MOON_MASS)*MOON_RP/((MOON_RA+MOON_RP)*MOON_RA))  # speed at apogee
MOON_DENSITY = MOON_MASS/(4/3*pi*MOON_RADIUS**3)

#calculation speed
DT = 1
ITERATIONS = 4