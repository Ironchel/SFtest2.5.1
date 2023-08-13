
from players import Players
import random


class AI(Players):
    """Computer player class for receiving shot points and placing ships from the computer"""
    list_alp = ['A', 'B', 'C', 'D', 'E', 'F']
    list_num = ['1', '2', '3', '4', '5', '6']

    def random_step(self):
        """The function determines a random point from the computer and returns it"""
        step_1 = random.choice(self.list_alp)
        step_2 = random.choice(self.list_num)
        step_3 = round(random.random())
        return  [step_1,step_2,step_3]

    def ship_and_dot_AI(self,type_ship, step):
        """The function determines the installation points of the ships and
         the shot for the computer's move based on the input from the random_step function"""
        litters = 0
        nummers = 0
        index_ship_alp = self.list_alp.index(step[0])
        index_ship_num = self.list_num.index(step[1])
        list_ship = []
        if self.list_alp.index(step[0]) > 2:
            litters = 1
        if self.list_num.index(step[1]) > 2:
            nummers = 1
        for item in range(type_ship):
            if step[2] == 0:
                if nummers == 0:
                    list_ship.append([step[0],self.list_num[index_ship_num+item]])
                else:
                    list_ship.append([step[0],self.list_num[index_ship_num-item]])
            else:
                if litters == 0:
                    list_ship.append([self.list_alp[index_ship_alp + item] , step[1]])
                else:
                    list_ship.append([self.list_alp[index_ship_alp - item] , step[1]])
        list_ship.sort()
        return list_ship
