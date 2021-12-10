"""
--------------------------
Geometry utility functions
--------------------------
"""
import math

def circle_area(radius: int | float) -> float:
    """ Returns the area of a 2D circle """
    return math.pi * radius**2

def circumference(radius: int | float) -> float:
    """ Returns the Circumference of a 2D circle """
    return 2 * math.pi * radius

def sphere_volume(radius: int | float) -> float:
    """ Returns the volume of a 3D sphere """
    return (4/3) * math.pi * radius**3

def sphere_sa(radius: int | float) -> float:
    """ Returns the SA of a 3D sphere """
    return 4 * math.pi * radius**2

def cylinder_volume(radius: int | float, height: int | float) -> float:
    """ Returns the volume of a cylinder """
    return math.pi * radius**2 * height

def cylinder_sa(radius: int | float, height: int | float) -> float:
    """ Returns the SA of a cylinder """
    return 2 * math.pi * radius * height + 2 * math.pi * radius**2

def cone_volume(radius: int | float, height: int | float) -> float:
    """ Returns the volume of a cone """
    return math.pi * radius**2 * (height/3)

def cone_l_SA(radius: int | float, length: int | float) -> float:
    """ Returns the SA of a cone, given its LENGTH (not vertical height) """
    return math.pi * radius**2 + math.pi * radius * length

def hypotenuse(a: int | float, b: int | float) -> float:
    """ Returns the hypotenuse of RA triangle using pythag """
    return (a**2 + b**2)**(1/2)


