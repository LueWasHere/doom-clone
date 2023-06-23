import math
def rotate_around_origin(point: tuple, rotation: int=0, size=(600, 600)) -> tuple: # the point will be pygame coords so we hve to convert it
    point = (point[0]-size[0]/2,-(point[1])+size[1]/2,point[-1])
    rotation_in_radians = rotation/6.28318531
    x_coord = (math.sin(rotation_in_radians)*point[0])+(math.cos(rotation_in_radians)*point[1])
    y_coord = math.sin(rotation_in_radians)*point[1]
    return (y_coord+size[0]/2, -(x_coord)+size[1]/2)

# The code below was to test an idea I had with fetching map data from the map (See the __init__ function in rendering.world.World or see the fetch function in utils.read_game_file.MapData)
"""class stuff: # ! REMOVE
    def __init__(self) -> None:
        self.list_s = []
    def fetch(self, to_fetch):
        return eval("self." + to_fetch)
    
things = stuff()
print(things.fetch("list_s"))"""