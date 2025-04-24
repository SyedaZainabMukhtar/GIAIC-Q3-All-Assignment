"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""

# Gravitational constants
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
    # Get weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))

    # Ask for planet name
    planet = input("Enter a planet: ")

    # Choose gravity constant based on planet
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    else:
        gravity_constant = NEPTUNE_GRAVITY

    # Calculate and round weight
    planetary_weight = earth_weight * gravity_constant
    rounded_weight = round(planetary_weight, 2)

    # Output result
    print("The equivalent weight on " + planet + ": " + str(rounded_weight))

if __name__ == "__main__":
    main()
