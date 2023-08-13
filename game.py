
from ship import Ship
from board import Board
from players import Players
from user import User
from ai import AI
from mistake import Mistake
from random import randint
import time



class Game:
    """
    🕜 🕑 🕝 🕒 🕞 🕓 🕟 🕔 🕠 🕕 🕡 🕖
     Добро пожалвать на игру морской бой
    👹 👺 👻 👽 👾 🤖 🧠 🦷 🦴 👀 👁 👅


    Вы можете выбрать с кем играть: Компьютером или с Игроком

    Компьютер имеет два уровня сложности: Сложный и Легкий

     Правила следующие:
     1) Вы размещаете все свои корабли по карте.

     У вас есть 3 вида кораблей:
     а) 3-х палубный - 1 шт
     б) 2-х палубный - 2 шт
     в) 1-х палубный - 4 шт

     Выставлять корабли вы можете в любом порядке.
     Сначало выбирайте тип корабля, затем указываете точки где хотите разместить корабль.
     Точки должны быть только латинскими буквами и начинаться с буквы затем цыфра
     Формат ввода (пример): Тип = 3 Точки = B3 C3 D3

     2) У вас есть две карты одна ваша (верхняя), другая противники (нижняя)
     Выставляйте корабли, а так же стреляйте в границе карты

     3) После раставления кораблей игроки можут начать огонь
     Как и с кораблями выбирайте точку (одну)
     Формат ввода (пример): Точка = F6
     Если попали по кораблю вы можете стрелять ещё раз

     4) Индикатры в игре:
     Пустое место =              '🔎'
     Промах ваш или противника = '💩'
     Попадание в корабль =       '💀'
     Ваш корабль =               '🤡'

     5) Игра длится до унижточение всех кораблей одного из игроков

     6) Начинает стрелять Игрок 1

     ⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛"""

    amount = 0
    antwort = 0
    def arrange_ships(self):
        """The function of installing all ships on the map from users"""
        while True:
            check_ship = 0
            print(f"Раставьте корабли согласно правилам {self.player_1_name}\n"
                  f"Это ваша карта")
            self.player_1.player_map.show_map()
            print("Это карта противника")
            self.player_1.player_map_enemy.show_map()
            while not check_ship:
                check_ship = Mistake.check_ship(self,*self.player_1.choose_place_ship())
            if self.player_1.move_ship(self.player_1.get_type(),check_ship):
                Mistake.more_print(self)
                time.sleep(4)
                continue
            self.ship_1 = Ship(self.player_1.get_type(),check_ship,1)
            self.player_1.set_list_area(self.ship_1.get_ship_area)
            self.player_1.player_map.installer_pic(self.ship_1.get_ship_dot(),4)
            print('Корабль создан')
            if not self.player_1.get_list_ship():
                break
        if self.amount:
            input("\n\n\n\n\nСейчас будет выбирать противник корабли.\n"
                  "Пожалуйста спрячьте свои корабли\n"
                  "Для продолжения введите что угодно\n\n\n\n")
            while True:
                check_ship = 0
                print(f"Раставьте корабли согласно правилам {self.player_2_name}\n"
                      f"Это ваша карта")
                self.player_2.player_map.show_map()
                print("Это карта противника")
                self.player_2.player_map_enemy.show_map()
                while not check_ship:
                    check_ship = Mistake.check_ship(self, *self.player_2.choose_place_ship())
                if self.player_2.move_ship(self.player_2.get_type(), check_ship):
                    Mistake.more_print(self)
                    time.sleep(4)
                    continue
                self.ship_2 = Ship(self.player_2.get_type(), check_ship,2)
                self.player_2.set_list_area(self.ship_2.get_ship_area)
                self.player_2.player_map.installer_pic(self.ship_2.get_ship_dot(), 4)
                print('Корабль создан')
                if not self.player_2.get_list_ship():
                    break
            input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nИгра начинается\n\n"
                      "Пожалуйста спрячьте свои корабли\n\n"
                      "Для продолжения введите что угодно\n\n: ")
            self.shooting(self)

    def choice_two_players(self):
        """Function for entering usernames and creating a user class"""
        print("\nВведите Ваши имена. Сначала, Игрок 1")
        self.player_1_name = input(': ')
        print("\nТеперь Игрок 2\n")
        self.player_2_name = input(': ')
        print("\nРаставляйте все корабли по очереди\n")
        self.player_1 = User()
        self.player_2 = User()
        self.amount = 1
        self.arrange_ships(self)

    def choice_AI_player(self):
        """Function for playing with the computer,
        starts the installation of the user's ships and
        arranges the computer's ships automatically"""
        print("\nВведите Ваше имя.")
        self.player_1_name = input(': ')
        self.player_1 = User()
        self.arrange_ships(self)
        ship_AI = [3,2,2,1,1,1,1]
        while True:
            self.player_AI = AI()
            count = 0
            for item in ship_AI:
                while count !=500:
                    check_ship = self.player_AI.ship_and_dot_AI(item,self.player_AI.random_step())
                    check_move = self.player_AI.move_ship(item, check_ship)
                    if check_move:
                        count += 1
                        continue
                    else:
                        break
                if count == 500:
                    break
                self.ship_AI = Ship(item, check_ship,3)
                self.player_AI.set_list_area(self.ship_AI.get_ship_area)
                self.player_AI.player_map.installer_pic(self.ship_AI.get_ship_dot(), 4)
            if count == 500:
                continue
            break
        print("Корабли компьютера созданы")
        self.shooting(self)

    def shooting(self):
        """Feature shots, from users and from the computer. However, it is a cycle of player moves.
            In fact, the main function that runs other parts of the code.
            And also, when the condition of victory is reached, it shows the winner"""
        count_ship_AI_dest = 0
        count_ship_player_1_dest =0
        count_ship_player_2_dest =0
        winner = ""
        if self.antwort == 2:
            for item in self.player_1.get_ship_player_area():
                if item not in self.player_1.get_ship_player():
                    self.player_AI.move_shot([item])
        while (count_ship_player_1_dest != 11
               and count_ship_player_2_dest != 11
               and count_ship_AI_dest != 11):
            input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{self.player_1_name} выбирает точку выстрела\n"
                  f"Для продолжения введите что угодно\n : ")
            while True:
                print(f"Это карта игрока - {self.player_1_name}")
                self.player_1.player_map.show_map()
                print(f"Это карта противника игрока - {self.player_1_name}")
                self.player_1.player_map_enemy.show_map()
                shot_dot_player_1 = self.player_1.choose_place_dot()
                check_dot = Mistake.check_dot(self,shot_dot_player_1)
                if not check_dot:
                    continue
                shot = self.player_1.move_shot(check_dot)
                if not shot:
                    print("\nВы уже сюда стреляли\n")
                    continue
                dot = self.player_1.get_move_shot()
                if self.amount:
                    if dot[0] in self.player_2.get_ship_player():
                        self.player_2.player_map.installer_pic(dot, 3)
                        self.player_1.player_map_enemy.installer_pic(dot, 3)
                        self.player_2.set_ship_player(dot)
                        print(f"Это карта игрока - {self.player_1_name}")
                        self.player_1.player_map.show_map()
                        print(f"Это карта противника игрока - {self.player_1_name}")
                        self.player_1.player_map_enemy.show_map()
                        check_ship = self.ship_2.check_ship(dot[0])
                        time.sleep(3)
                        count_ship_player_1_dest += 1
                        if check_ship and count_ship_player_1_dest != 11:
                            break
                        if count_ship_player_1_dest == 11:
                            winner = f'{self.player_1_name}'
                            break
                        continue
                    else:
                        self.player_2.player_map.installer_pic(dot, 2)
                        self.player_1.player_map_enemy.installer_pic(dot, 2)
                        print(f"Это карта игрока - {self.player_1_name}")
                        self.player_1.player_map.show_map()
                        print(f"Это карта противника игрока - {self.player_1_name}")
                        self.player_1.player_map_enemy.show_map()
                        print("\nМимо\n")
                        time.sleep(3)
                        break
                else:
                    if dot[0] in self.player_AI.get_ship_player():
                        self.player_AI.player_map.installer_pic(dot, 3)
                        self.player_1.player_map_enemy.installer_pic(dot, 3)
                        self.player_AI.set_ship_player(dot)
                        print(f"Это карта игрока - {self.player_1_name}")
                        self.player_1.player_map.show_map()
                        print(f"Это карта противника игрока - {self.player_1_name}")
                        self.player_1.player_map_enemy.show_map()
                        check_ship = self.ship_AI.check_ship( dot[0])
                        time.sleep(3)
                        count_ship_player_1_dest += 1
                        if check_ship and count_ship_player_1_dest != 11:
                            break
                        if count_ship_player_1_dest == 11:
                            winner = f'{self.player_1_name}'
                            break
                        continue
                    else:
                        self.player_AI.player_map.installer_pic(dot, 2)
                        self.player_1.player_map_enemy.installer_pic(dot, 2)
                        print(f"Это карта игрока - {self.player_1_name}")
                        self.player_1.player_map.show_map()
                        print(f"Это карта противника игрока - {self.player_1_name}")
                        self.player_1.player_map_enemy.show_map()
                        print("\nМимо\n")
                        time.sleep(3)
                        break
            if self.amount  and (count_ship_player_1_dest != 11
               and count_ship_player_2_dest != 11
               and count_ship_AI_dest != 11):
                input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{self.player_2_name} выбирает точку выстрела\n"
                      f"Для продолжения введите что угодно\n : ")
                print(f"Это карта игрока - {self.player_2_name}")
                self.player_2.player_map.show_map()
                print(f"Это карта противника игрока - {self.player_2_name}")
                self.player_2.player_map_enemy.show_map()
                while True:
                    shot_dot_player_2 = self.player_2.choose_place_dot()
                    check_dot = Mistake.check_dot(self,shot_dot_player_2)
                    if not check_dot:
                        continue
                    shot = self.player_2.move_shot(check_dot)
                    if not shot:
                        print("\nВы уже сюда стреляли\n")
                        continue
                    dot = self.player_2.get_move_shot()
                    if dot[0] in self.player_1.get_ship_player():
                        self.player_1.player_map.installer_pic(dot, 3)
                        self.player_2.player_map_enemy.installer_pic(dot, 3)
                        self.player_1.set_ship_player(dot)
                        count_ship_player_2_dest += 1
                        print(f"Это карта игрока - {self.player_2_name}")
                        self.player_2.player_map.show_map()
                        print(f"Это карта противника игрока - {self.player_2_name}")
                        self.player_2.player_map_enemy.show_map()
                        check_ship = self.ship_1.check_ship( dot[0])
                        time.sleep(3)
                        if check_ship and count_ship_player_2_dest != 11:
                            break
                        if count_ship_player_2_dest == 11:
                            winner = f'{self.player_2_name}'
                            break
                        continue
                    else:
                        self.player_1.player_map.installer_pic(dot, 2)
                        self.player_2.player_map_enemy.installer_pic(dot, 2)
                        print(f"Это карта игрока - {self.player_2_name}")
                        self.player_2.player_map.show_map()
                        print(f"Это карта противника игрока - {self.player_2_name}")
                        self.player_2.player_map_enemy.show_map()
                        print("\nМимо\n")
                        time.sleep(3)
                        break
            elif (count_ship_player_1_dest != 11
               and count_ship_player_2_dest != 11
               and count_ship_AI_dest != 11):
                while True:
                    shot_dot_player_AI = self.player_AI.ship_and_dot_AI(1,self.player_AI.random_step())
                    shot = self.player_AI.move_shot(shot_dot_player_AI)
                    if not shot:
                        continue
                    dot = self.player_AI.get_move_shot()
                    if dot[0] in self.player_1.get_ship_player():
                        self.player_1.player_map.installer_pic(dot, 3)
                        self.player_1.set_ship_player(dot)
                        count_ship_AI_dest += 1
                        self.player_1.player_map.show_map()
                        print("\n🥁Ход Компьютера🥁\n")
                        print(f"Это карта игрока - {self.player_1_name}")
                        self.player_1.player_map.show_map()
                        check_ship = self.ship_1.check_ship( dot[0])
                        time.sleep(3)
                        if check_ship and count_ship_AI_dest != 11:
                            print("\nХод компьютера завершен\n")
                            time.sleep(4)
                            break
                        if count_ship_AI_dest == 11:
                            winner = 'Computer'
                            break
                        continue
                    else:
                        self.player_1.player_map.installer_pic(dot, 2)
                        self.player_AI.player_map_enemy.installer_pic(dot, 2)
                        print("\n🥁Ход Компьютера🥁\n")
                        print(f"Это карта игрока - {self.player_1_name}")
                        self.player_1.player_map.show_map()
                        print("Мимо")
                        print("\nХод компьютера завершен\n")
                        time.sleep(4)
                        break
        print(f"\n\n\n\n\nИтоговая карта игрока  - 😎{self.player_1_name}😎\n")
        self.player_1.player_map.show_map()
        if self.amount:
            print(f"\n\nИтоговая карта игрока  - 🧓{self.player_2_name}🧓\n")
            self.player_2.player_map.show_map()
        else:
            print(f"\n\nИтоговая карта игрока  - 🥁'Computer'🥁\n")
            self.player_AI.player_map.show_map()
        print(f"\n\n\n📣📣📣📣📣📣📣📣📣📣📣📣📣📣📣📣📣📣📣📣\n"
              f"\t\t  Побеждает - {winner}\n"
              f"📣📣📣📣📣📣📣📣📣📣📣📣📣📣📣📣📣📣📣📣\n\n\n")


    def nummers_of_players(self):
        """The function asks the user to select a game mode"""
        print('\n\n')
        while True:
            try:
                antwort = int(input("Играть вдваем или с компьютером\n"
                      "Введите 1 Играть с Компьютером\n"
                      "Введите 2 Играть на двоих\n"
                      "Ответ: "))
                if antwort == 1:
                    antwort = str(input("Какой уровень сложности?\n"
                                    "Введите 1 Легкий\n"
                                    "Введите 2 Сложный\n"
                                      "Ответ: "))
                if 0 < int(antwort) < 3:
                    break
                else:
                    print('\nНет таких опциий\n')
                    continue
            except:
                print('\nВведите пожалуйста цифры!!!!!\n')
                continue
        if isinstance(antwort, int):
            self.choice_two_players(self)
        else:
            self.antwort = int(antwort)
            self.choice_AI_player(self)


    def start(self):
        """The function to start the game, shows the rules and runs the main code"""
        print(Game.__doc__)
        input('Для продолжения введите что угодно.\nНачнем? :')
        self.nummers_of_players(self)


a= Game
a.start(a)






