import unittest

# main.py исключён из тестирования в .coveragerc
from bag import Bag
from card import Card
from player import Player
from game import Lotto


class Test(unittest.TestCase):

    def test_bag(self):
        bag = Bag()
        test_bag = Bag()
        self.assertTrue(bag == test_bag)
        self.assertEqual(len(bag._bag), 90)
        self.assertTrue(bag.get_barrel())
        self.assertFalse(bag == test_bag)
        self.assertTrue(bag != test_bag)
        self.assertEqual(len(bag), 89)
        for i in range(len(bag)):
            bag.get_barrel()
        self.assertEqual(bag.get_barrel(), 0)
        self.assertEqual(str(bag), '')

    def test_card(self):
        card = Card()
        test_card = Card()
        self.assertEqual(len(str(card).split(', ')), 15)
        self.assertListEqual([len(item) for item in card._card], [9, 9, 9])
        self.assertEqual(len(card), 15)
        self.assertTrue(card.check_barrel(list(set(card._card[0]))[1]))
        self.assertEqual(len(card), 14)
        self.assertTrue(card != test_card)
        self.assertFalse(card.check_barrel(99))
        self.assertEqual(len(card.get_card()), 3)

    def test_player(self):
        player = Player('test player', True)
        test_player = Player('test player 2', True)
        self.assertEqual(str(player), 'Игрок: test player, незакрытых номеров: 15, компьютер')
        self.assertEqual(player.name, 'test player')
        self.assertTrue(player.is_comp)
        self.assertEqual(len(player.show_card()), 5)
        self.assertFalse(player.check_barrel(99))
        player.check_barrel(int(str(player.card).split(', ')[0]))
        self.assertEqual(len(player), 14)
        self.assertFalse(player == test_player)
        self.assertTrue(player > test_player)

    def test_game(self):
        game = Lotto()
        self.assertEqual(game._num_players, 0)
        self.assertEqual(game._tot_players, 0)
        self.assertListEqual(game._players, [])
        self.assertTrue(game._all_comp)
        self.assertEqual(game._set_num_players(2), None)
        self.assertEqual(game._num_players, 2)
        self.assertTrue(game._set_players_name(True))
        self.assertEqual(str(game), 'Игроков: 2, осталось бочонков: 90')
        game._players[0].loose = True
        game._players[1].loose = True
        game._tot_players = 0
        game._bag._bag = []
        self.assertFalse(game._next_turn())
        test_game = Lotto()
        self.assertEqual(test_game._set_num_players(2), None)
        self.assertEqual(test_game._num_players, 2)
        self.assertTrue(test_game._set_players_name(True))
        self.assertFalse(game == test_game)
        self.assertEqual(len(game), 0)
