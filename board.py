

class Board:
    """The class creates a field (map) for players, and also changes it"""
    field_unknown_1 = '🔎'
    field_miss_2 = '💩'
    field_hit_3 = '💀'
    field_ship_4 = '🤡'
    field_delimiter = '-----------------------------------------------'
    a_1 = '   │   A  │   B  │   C   │   D  │   E  │   F  │'

    def __init__(self):
        self.map = self.get_clear_map()

    @classmethod
    def get_clear_map(cls):
        """The function generates the player's field and the opponent's field for each player"""
        list_alp = ['A','B','C','D','E','F']
        a = [[[  str(erste+1),str(list_alp[i]),cls.field_unknown_1] for i in range(6)] for erste in range(6)]
        c = []
        for item in a:
                c += item
        return sorted(c)

    def show_map(self):
        """The function shows the map of the players and the opponent"""
        view_map = ""
        count = 0
        verify_symbol = 0
        print(self.a_1)
        print(self.field_delimiter)
        for item_1,item_2,item_3 in self.map:
            if item_1 != verify_symbol:
                count += 1
                if verify_symbol:
                    view_map += " " +"│" + '\n' + self.field_delimiter + "\n"
                verify_symbol = item_1
                view_map += " "   + str(count)
            view_map += " "   + "│"  +"  " + item_3 + ' '
        print(view_map + " │")

    def installer_pic(self,dot,kind):
        """The function sets the player's choice and changes the player's field"""
        change_kind = 0
        if kind == 1:
            change_kind = self.field_unknown_1
        elif kind == 2:
            change_kind = self.field_miss_2
        elif kind == 3:
            change_kind = self.field_hit_3
        else:
            change_kind = self.field_ship_4
        count = -1
        count_2 = 0
        dot.sort()
        for item_1, item_2, item_3 in self.map:
            count += 1
            if count_2 != len(dot) and dot[count_2][0] in item_2:
                if dot[count_2][1] in item_1:
                    count_2 += 1
                    # if isinstance(dot, Ship):
                    self.map[count][2] = (
                        self.map[count][2].replace(
                            self.map[count][2], change_kind))
