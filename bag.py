import random


class Bag:
    def __init__(self):
        self._bag = list(range(1, 91))  # доступные номера в мешке

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

    def barrels_left(self) -> int:
        return len(self._bag)
