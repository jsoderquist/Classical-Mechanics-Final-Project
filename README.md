# Classical-Mechanics-Final-Project
Tearing the Moon with Tidal Forces and Watching its Orbit


Known Issues:

move_earth_action:
Problem: The Earth is moved before the moon calculates its acceleration. This creates perpetual motion by adding energy to the system.
Proposed Solution: Calculate all accelerations in one class and then change all the positions in move_earth_action and move_moon_action.
Current Implementation: The Earth doesn't move. The simulation acts as if the moon is in a Kepler orbit

collisions_action:
Problem: The simulation is aborted occasionally because it tries to remove an object that it has already removed.
Proposed Solution: Currently unknown
Current Implementation: pieces of debris never recombine
