import card


class Player:
    def __init__(self, name, is_comp):
        self.name = name         # имя игрока
        self.is_comp = is_comp   # True - игрок это компьютер, False - человек
        self.card = card.Card()  # карточка игрока
        self.loose = False       # флаг проигрыша игрока

    def show_card(self):
        """
        генерирует карточку игрока для вывода на экран
        :return:
        """
        result = list()
        result.append('┌── ' + self.name + ' ' + '─' * (32 - len(self.name)) + '┐')
        for i in self.card.get_card():
            result.append('│ ' + ''.join(i) + ' │')
        result.append('└' + '─' * 36 + '┘')
        return result

    def check_barrel(self, barrel) -> bool:
        """
        проверяет, есть ли бочонок у игрока в карточке
        :param barrel:
        :return:
        """
        return self.card.check_barrel(barrel)
