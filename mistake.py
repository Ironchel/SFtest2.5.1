

class Mistake:
    """Class for checking input errors from the user when firing or placing a ship"""
    def check_ship(self, type_ship, dot_ship):
        """The function checks for input errors from the user when placing a ship"""
        list_alp = ['A', 'B', 'C', 'D', 'E', 'F', '1', '2', '3', '4', '5', '6']
        try:
            type_ship = int(type_ship)
            ship_split = "".join(dot_ship.split())
            ship_gen_list = [[ship_split[item - 1], ship_split[item]]
                             for item in range(1, len(ship_split), 2)]
            ship_gen_list.sort()
            check_list_alp = []
            check_list_num = []
            index_alp = []
            index_num = []
            for item in ship_gen_list:
                if item[0].isalpha():
                    index_alp.append(list_alp.index(item[0]))
                    check_list_alp.append(item[0])
                    if item[1].isdigit():
                        index_num.append(list_alp.index(item[1]))
                        check_list_num .append(item[1])
                    else:
                        print("Поставте пожалуйста Сначало букву, потом цифру")
                        return False
                else:
                    print("Поставте пожалуйста Сначало букву, потом цифру")
                    return False
            if check_list_alp.count(check_list_alp[0]) == type_ship:
                if (len(index_num) == 3 and index_num[0] + 1 == index_num[1] == index_num[2] -1
                        or len(index_num) == 2 and index_num[0] + 1 == index_num[1]
                        or len(index_num) == 1):
                    return ship_gen_list
                else:
                    print("Корабль должен быть целым) он так не изгибается")
                    return False
            elif check_list_num.count(check_list_num[0]) == type_ship:
                if (len(index_alp) == 3 and index_alp[0] + 1 == index_alp[1] == index_alp[2] - 1
                        or len(index_alp) == 2 and index_alp[0] + 1 == index_alp[1]
                        or len(index_alp) == 1):
                    return ship_gen_list
                else:
                    print("Корабль должен быть целым) он так не изгибается")
                    return False
            else:
                print("Вам нужно ввести тип корабля, укажите пожалуйста тип правильной цифрой\n"
                      "А так же, тип коробля должен совпадать с количеством точек корабля")
                return False
        except:
            print("Укажите пожалуйста верные координаты корабля.\nНе забудьте вводить данные только латинским алфавитом"
                  "Так же, вам нужно ввести тип корабля, укажите пожалуйста тип правильной цифрой\n"
                      "А так же, тип коробля должен совпадать с количеством точек корабля")
            return False




    def check_dot(self, dot):
        """The function checks for input errors from the user when fired"""
        list_alp = ['A', 'B', 'C', 'D', 'E', 'F', '1', '2', '3', '4', '5', '6']
        try:
            if len(dot) == 2 and dot[0].isalpha() and dot[1].isdigit() and dot[0] in list_alp and dot[1] in list_alp:
                list_dot = [[dot[0], dot[1]]]
                return  list_dot
            else:
                print("Пожалуйста укажите верные кординаты. Первая буква, вторая цыфра и без других знаков\n"
                      "Так же в координаты должны быть в карте")
                return False
        except:
            print('Что-то вы не правильно вводите')
            return False

    def more_print(self):
        """The function shows the user what types of ships he can place, in case of an input error"""
        print("\n"
              "🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\nНапоминаем, что вы можете иметь:"
              "3-х палубный - 1 корабль"
              "2-х палубный - 2 корабля"
              "1-о палубный - 4 корабля\n"
              "А так же расстояние должно быть от них в одну клетку\n"
              "🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n")
