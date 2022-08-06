import unittest

# main.py исключён из тестирования в .coveragerc
from bag import Bag
from card import Card
from player import Player
from game import Lotto


class Test(unittest.TestCase):

    def test_bag(self):
        bag = Bag()
        self.assertEqual(len(bag._bag), 90)
        self.assertTrue(bag.get_barrel())
        self.assertEqual(bag.barrels_left(), 89)
        for i in range(89):
            bag.get_barrel()
        self.assertEqual(bag.get_barrel(), 0)

    def test_card(self):
        card = Card()
        self.assertListEqual([len(item) for item in card._card], [9, 9, 9])
        self.assertEqual(card.num_left(), 15)
        self.assertTrue(card.check_barrel(list(set(card._card[0]))[1]))
        self.assertEqual(card.num_left(), 14)
        self.assertFalse(card.check_barrel(99))
        self.assertEqual(len(card.get_card()), 3)

    def test_player(self):
        player = Player('test player', True)
        self.assertEqual(player.name, 'test player')
        self.assertTrue(player.is_comp)
        self.assertEqual(len(player.show_card()), 5)
        self.assertFalse(player.check_barrel(99))

    def test_game(self):
        game = Lotto()
        self.assertEqual(game._num_players, 0)
        self.assertEqual(game._tot_players, 0)
        self.assertListEqual(game._players, [])
        self.assertTrue(game._all_comp)
        self.assertEqual(game._set_num_players(2), None)
        self.assertEqual(game._num_players, 2)
        self.assertTrue(game._set_players_name(True))
        game._players[0].loose = True
        game._players[1].loose = True
        game._tot_players = 0
        game._bag._bag = []
        self.assertFalse(game._next_turn())
