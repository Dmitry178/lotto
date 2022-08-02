import player
import bag


class Lotto:
    def __init__(self):
        self._num_players = 0  # количество игроков, Можно убрать и высчитывать из len(self.players)
        self._tot_players = 0  # количество игроков за минус выбывших в игре
        self._players = []  # список игроков
        self._bag = bag.Bag()  # мешок с бочонками
        self._all_comp = True  # указывает, все ли игроки - компьютер

    def _set_num_players(self):
        """
        ввод числа игроков
        :return:
        """

        while True:
            try:
                players = int(input('Выберите число игроков от 2 до 8 (0 - выход): '))
                if not players or 1 < players < 9:
                    break
            except:
                pass

        self._num_players = players
        self._tot_players = players

    def _set_players_name(self):
        """
        ввод имён игроков (не проверяются повторения имён)
        :return:
        """

        if not self._num_players:
            return

        comp_idx = 1
        print('\nВведите имена игроков (без имени - компьютер): ')
        for i in range(self._num_players):
            name = input(f'Игрок {i + 1}: ')
            is_comp = not name

            if not name:
                name = 'Компьютер ' + str(comp_idx)
                comp_idx += 1
            else:
                self._all_comp = False

            self._players.append(player.Player(name, is_comp))

    def _next_turn(self) -> bool:
        barrel = self._bag.get_barrel()
        num_barrels = self._bag.barrels_left()
        print()
        print(f'Новый бочонок: {barrel}, осталось: {num_barrels}')
        for pl in self._players:
            if pl.loose:  # пропускаем проигравшего игрока
                continue
            pl.show_card()  # выводим карточку игрока

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

            if not pl.card.num_left():  # если закрыта вся карточка
                print(f'Игрок {pl.name} выйграл!')
                return False

            if self._tot_players == 1:  # если все игроки выбыли и остался только один
                for p in self._players:
                    if not p.loose:
                        print(f'Игрок {p.name} выйграл!')
                        return False

        input('Ход сделан, нажмите ENTER для продолжения')

        if not num_barrels:
            return False

        return True

    def start(self):
        """
        запуск игры
        :return:
        """
        print('\nИгра Лото')
        self._set_num_players()
        if not self._num_players:
            return

        self._set_players_name()

        while self._next_turn():
            pass
