import random


class Card:
    def __init__(self):
        self._card = []
        self._generate_card()
        self._num_left = 15  # количество незакрытых номеров
        # self.card = self._card

    def _generate_card(self):
        """
        создание карточки
        :return:
        """
        self._card = []
        initial_list = list(range(1, 91))  # изначальный набор данных 1..90

        for i in range(3):
            # случайная выборка 5 элементов из изначального набора
            lst1 = random.sample(initial_list, 5)

            # убираем выбранные элементы из изначального набора
            initial_list = [item for item in initial_list if item not in lst1]

            # из оставшегося набора делаем выборку ещё из 4 элементов
            lst2 = random.sample(initial_list, 4)

            # соединяем два списка, убираем из суммарного отсортированного списка элементы lst2, повторяем 3 раза
            # на выходе получаем 9x3 карточку игрока с 5ю значениями в каждой линии
            result_line = []
            for m in sorted(lst1 + lst2):
                result_line.append(m if m in lst1 else 0)

            self._card.append(result_line)

    def get_card(self):
        """
        выдаёт карточку
        :return:
        """
        result = []
        for i in self._card:
            st = '  '.join([' ' + str(st) if st < 10 else str(st) for st in i])
            st = st.replace(' 0', '  ').replace(' -1', '--')
            result.append(st)
        return result

    def check_barrel(self, barrel) -> bool:
        """
        проверка бочонка в карточке
        :return:
        """
        result = False
        for i in self._card:
            if barrel in i:
                find = i.index(barrel)
                i[find] = -1
                self._num_left -= 1
                result = True

        return result

    def num_left(self) -> int:
        """
        возвращает количество оставшихся незакрытых номеров
        :return:
        """
        return self._num_left
