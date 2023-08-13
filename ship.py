
class Ship:
    """Ship class. Creates a ship zone and checks if the ship has been hit"""
    ship_destroy_1 = []
    ship_destroy_2 = []
    ship_destroy_AI = []

    def __init__(self, ship_size_hp, ship_dot,player_num):
        self.ship_dot = ship_dot
        self.ship_size_hp = ship_size_hp
        self.player_num = player_num
        if player_num == 1:
            self.ship_destroy_1.append(ship_dot)
        elif player_num ==2:
            self.ship_destroy_2.append(ship_dot)
        else:
            self.ship_destroy_AI.append(ship_dot)


    @property
    def get_ship_area(self): # area ship return list
        """The function creates a ship zone"""
        list_alp = ['A', 'B', 'C', 'D', 'E', 'F']
        list_area = []
        for dot in self.ship_dot:
            b = list_alp.index(dot[0])
            c = int(dot[1])
            g = [[[list_alp[j], str(i)] for j in range(b - 1, b + 2) if j < 6 and j >= 0]
                 for i in range(c - 1, c + 2) if i < 7 and i > 0]
            for item_1 in g:
                for item_2 in item_1:
                    if item_2 not in list_area:
                        list_area.append(item_2)
        return list_area

    def get_ship_dot(self):
        return self.ship_dot

    def check_ship(self, dot_b):
        """The function checks if there is a hit on the ship"""
        if self.player_num == 1:
            list_count = self.ship_destroy_1
        elif self.player_num == 2:
            list_count = self.ship_destroy_2
        else:
            list_count = self.ship_destroy_AI
        for index_num, item in enumerate(list_count, 0):
            if dot_b in item:
                list_count[index_num].remove(dot_b)
                break
        if not list_count[index_num]:
            print("Корабль уничтожен")
            return True
        else:
            print("Ранили корабль")
            return False



