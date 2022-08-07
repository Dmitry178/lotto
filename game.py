import player
import bag


class Lotto:
    def __init__(self):
        self._num_players = 0  # количество игроков, Можно убрать и высчитывать из len(self.players)
        self._tot_players = 0  # количество игроков за минус выбывших в игре
        self._players = []  # список игроков
        self._bag = bag.Bag()  # мешок с бочонками
        self._all_comp = True  # указывает, все ли игроки - компьютер

    def __str__(self):
        return 'Игроков: ' + str(len(self._players)) + ', осталось бочонков: ' + str(len(self._bag))

    def __len__(self):
        """
        длина класса будет означать количество оставшихся бочонков
        :return:
        """
        return len(self._bag)

    def __eq__(self, other):
        """
        этот класс сравнивается по количеству оставшихся бочонков
        :param other:
        :return:
        """
        return len(self) == len(other)

    def _set_num_players(self, default=2):
        """
        ввод числа игроков
        :param default: число игроков по умолчанию
        :return:
        """

        while True:
            try:
                if not default:
                    players = int(input('Выберите число игроков от 2 до 8 (0 - выход): '))
                else:
                    players = default
                if not players or 1 < players < 9:
                    break
            except:
                pass

        self._num_players = players
        self._tot_players = players

    def _set_players_name(self, default=False):
        """
        ввод имён игроков (не проверяются повторения имён)
        :param default: True, если имена игроков по умолчанию
        :return:
        """

        if not self._num_players:
            return

        comp_idx = 1
        if not default:
            print('\nВведите имена игроков (без имени - компьютер): ')

        for i in range(self._num_players):
            if not default:
                name = input(f'Игрок {i + 1}: ')
            else:
                name = ''

            is_comp = not name

            if not name:
                name = 'Компьютер ' + str(comp_idx)
                comp_idx += 1
            else:
                self._all_comp = False

            self._players.append(player.Player(name, is_comp))

        return True

    def _next_turn(self) -> bool:
        barrel = self._bag.get_barrel()
        num_barrels = len(self._bag)

        if num_barrels:
            print()
            print(f'Новый бочонок: {barrel}, осталось: {num_barrels}')

        for pl in self._players:
            if pl.loose:  # пропускаем проигравшего игрока
                continue
            for item in pl.show_card():  # выводим карточку игрока
                print(item)

        for pl in self._players:

            if pl.loose:  # пропускаем проигравшего игрока
                continue

            if not pl.is_comp:  # если игрок - человек
                cross_out = input(f'Игрок {pl.name}, зачеркнуть цифру {barrel}? (y - да, иначе - нет) ').lower() == 'y'
                num_exists = pl.check_barrel(barrel)

                if cross_out and num_exists:
                    print(f'Игрок {pl.name} зачеркнул цифру {barrel}')

                if cross_out and not num_exists:
                    print(f'Игрок {pl.name} зачеркнул цифру {barrel}, но она отсутствует в карточке')
                    print(f'Игрок {pl.name} проиграл')
                    self._tot_players -= 1
                    self._players[self._players.index(pl)].loose = True  # установка флага проигравшего игрока

                if not cross_out and num_exists:
                    print(f'Игрок {pl.name} не зачеркнул цифру {barrel}, но она присутствует в карточке')
                    print(f'Игрок {pl.name} проиграл')
                    self._tot_players -= 1
                    self._players[self._players.index(pl)].loose = True  # установка флага проигравшего игрока
            else:
                if pl.check_barrel(barrel):  # если игрок - компьютер
                    print(f'Игрок {pl.name} зачеркнул цифру {barrel}')

            if not len(pl.card):  # если закрыта вся карточка
                print(f'Игрок {pl.name} выйграл!')
                return False

            if self._tot_players == 1:  # если все игроки выбыли и остался только один
                for p in self._players:
                    if not p.loose:
                        print(f'Игрок {p.name} выйграл!')
                        return False

        if not num_barrels:
            return False

        input('Ход сделан, нажмите ENTER для продолжения')

        return True

    def start(self):
        """
        запуск игры
        :return:
        """
        print('\nИгра Лото')
        self._set_num_players(0)
        if not self._num_players:
            return

        self._set_players_name()

        while self._next_turn():
            pass
