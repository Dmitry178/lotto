import random


class Bag:
    def __init__(self):
        self._bag = list(range(1, 91))  # доступные номера в мешке

    def __len__(self):
        return len(self._bag)

    def __str__(self):
        return ', '.join([str(item) for item in self._bag])

    def __eq__(self, other):
        """
        сравнивается размер мешка, но не его содержимое
        :param other:
        :return:
        """
        return len(self) == len(other)

    def get_barrel(self) -> int:
        """
        достаём номер из мешка
        :return: номер из мешка, 0 если номера закончились
        """
        if not self._bag:
            return 0

        num = random.sample(self._bag, 1)
        self._bag.remove(num[0])

        return num[0]
