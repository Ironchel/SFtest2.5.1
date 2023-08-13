
from board import Board

class Players:
    """The player class automatically creates a player map,
    and also receives player moves during the game"""

    def __init__(self):
        self.player_map = Board()
        self.player_map_enemy = Board()
        self.player_ship = []
        self.player_ship_area = []
        self.player_list_dot = []
        self.list_ship_player = [3,2,2,1,1,1,1]


    def move_ship(self, hp_ship_player ,dot_ship_player):
        """The function takes points to create a ship and checks if the player has it"""
        if self.check_area_ship(dot_ship_player) and hp_ship_player in self.list_ship_player:
            self.list_ship_player.remove(hp_ship_player)
            for item in dot_ship_player:
                self.player_ship.append(item)
            return False
        else:
            return  True

    def move_shot(self, shot_player):
        """The function takes the points of the shot and
        checks if the shot was made at this point before"""
        if shot_player[0] not in self.player_list_dot:
            self.shot_player = shot_player
            self.player_list_dot.append(shot_player[0])
            return True
        else:
            return  False


    def get_move_shot(self):
        """The function returns the shot points"""
        return  self.shot_player

    def get_list_ship(self):
        """The function returns a list of ships that the player can install"""
        return self.list_ship_player


    def check_area_ship(self, dot):
        """The function checks the player's ship area to install another ship"""
        for item in dot:
            if item in self.player_ship_area:
                return False
        return True

    def set_list_area(self, ship):
        """The function to get zone from installed ship"""
        for item in ship:
            if item not in self.player_ship_area:
                self.player_ship_area.append(item)

    def get_ship_player(self):
        """The function returns a list of the player's ships"""
        return self.player_ship
    def get_ship_player_area(self):
        """The function returns the zone of all the player's ships"""
        return self.player_ship_area

    def set_ship_player(self, dot):
        """The function removes a ship point from the list if it was shot at"""
        self.player_ship.remove(dot[0])






