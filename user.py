from players import Players
class User(Players):
    """User class for accepting input from the user"""
    antwort_user_type = 0

    def choose_place_ship(self):
        """The function asks the user to enter points for placing ships and returns them"""
        print('\t\t\tГде будет место корабля?\n\tФормат:\n'
              '1) Тип \t- 3 или 2 или 1'
              '\n2) Введите координаты, через пробел - A1 A2 A3')
        print()
        print(' \t\t\t ↓ ↓ ↓')
        antwort_user_type = input('Сначало тип : ')
        print('       \t\t\t   ↓ ↓ ↓')
        antwort_user_dot = input('Теперь координаты : ').upper()
        self.antwort_user_type = antwort_user_type
        return antwort_user_type, antwort_user_dot

    def get_type(self):
        """The function returns a response from the user about the type of ship"""
        return int(self.antwort_user_type)

    def choose_place_dot(self):
        """The function asks the user for points to shoot and returns them."""
        print("Куда хотите запульнуть.\n"
              "Формат: A1\n"
              "Куда стреляем?")
        print()
        print('  \t\t\t\t   ↓ ↓ ↓')
        antwort_user_dot = str(input('Координаты : ').upper())
        return  antwort_user_dot








