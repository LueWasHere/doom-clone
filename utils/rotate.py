import math
def rotate_around_origin(point: tuple, rotation: int=0, size=(600, 600)) -> tuple: # the point will be pygame coords so we hve to convert it
    point = (point[0]-size[0]/2,-(point[1])+size[1]/2,point[-1])
    rotation_in_radians = rotation/6.28318531
    x_coord = (math.sin(rotation_in_radians)*point[0])+(math.cos(rotation_in_radians)*point[1])
    y_coord = math.sin(rotation_in_radians)*point[1]
    return (y_coord+size[0]/2, -(x_coord)+size[1]/2)
def rotate_around_point(point: tuple, point_around: tuple, rotation: int=0, size=(600, 600)) -> tuple:
    point = (point[0]-size[0]/2,-(point[1])+size[1]/2,point[-1]) # point coords are in pygame coords and must be corrected
    point_around = (point_around[0]-size[0]/2,-(point_around[1])+size[1]/2,point_around[-1])
    # We can just kind off pretend we're rotating the point around the origin by subtracting the "point-to-rotate-around"'s coordinates from the "point-to-rotate"'s
    if point[0] > point_around[0]: # TODO
        pass
    rotation_in_radians = rotation/6.28318531
    x_coord = (math.sin(rotation_in_radians)*point[0])+(math.cos(rotation_in_radians)*point[1])
    y_coord = math.sin(rotation_in_radians)*point[1]
    return (y_coord+size[0]/2, -(x_coord)+size[1]/2)