class World: # purpose of the World class is to keep track of player and ai movement
    def __init__(self, map_data, player) -> None:
        self.map_data = map_data
        self.player = player
        self.ais = map_data.fetch("entity_list")
