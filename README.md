# Classical-Mechanics-Final-Project
Tearing the Moon with Tidal Forces and Watching its Orbit


To use:
Open _main_.py and run. To change the Moon's initial distance from Earth, change HA at the bottom of the file constants.py. DT and ITERATIONS can also be change in constants.py to choose how fast the simulation runs. DT is measured in seconds and is the time interval between each Euler's method calculation. ITERATIONS is how many calculations the simulation does before checking tidal forces and displaying the new positions.

Known Issues:

move_earth_action:
Problem: The Earth is moved before the moon calculates its acceleration. This creates perpetual motion by adding energy to the system.
Proposed Solution: Calculate all accelerations in one class and then change all the positions in move_earth_action and move_moon_action.
Current Implementation: The Earth doesn't move. The simulation acts as if the moon is in a Kepler orbit

collisions_action:
Problem: The simulation is aborted occasionally because it tries to remove an object that it has already removed.
Proposed Solution: Currently unknown
Current Implementation: pieces of debris never recombine
