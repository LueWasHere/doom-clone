# Read the map data stored in the map files
class MapData:
    def __init__(self) -> None:
        pass
    def fetch(self, to_fetch):
        return eval("self." + to_fetch)
def read(filename: str) -> MapData:
    # TODO: The file system needs to be developed!
    return map_gathered