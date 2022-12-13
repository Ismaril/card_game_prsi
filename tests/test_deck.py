import sys
import unittest
import constants as c

from deck import Deck
from card import card_template


class TestDeck(unittest.TestCase):

    def test_create_deck(self):
        Deck.create_deck()
        test_deck_ = []
        for color in c.COLORS_ALL:
            for value in c.NUMBERS_ALL:
                test_deck_.append(card_template(color, value))

        self.assertEqual(Deck.deck, test_deck_, True)

    def test_deck_shuffle(self):
        Deck.create_deck()
        deck_original = Deck.deck.copy()
        Deck.deck_shuffle()

        deck_shuffled = Deck.deck
        self.assertNotEqual(deck_original, deck_shuffled)

    def test_deck_cards_together(self):
        Deck.create_deck()
        Deck.deck_shuffle()
        self.assertIs(len(Deck.deck) > 0, True)
        self.assertIs(len(Deck.played_deck) == 0, True)

        Deck.played_deck.append(Deck.deck.pop())
        self.assertIs(len(Deck.deck) > 0, True)
        self.assertIs(len(Deck.played_deck) > 0, True)

        Deck.put_deck_cards_together()
        self.assertIs(len(Deck.deck) > 0, True)
        self.assertIs(len(Deck.played_deck) == 0, True)

    def test_take_next_card(self):
        Deck.create_deck()
        Deck.deck_shuffle()
        deck_copy = Deck.deck.copy()

        for _ in Deck.deck:
            card_a = deck_copy.pop(0)
            card_a_ = Deck.take_next_card()
            self.assertEqual(card_a, card_a_)

    def test_played_card(self):
        Deck.create_deck()
        Deck.deck_shuffle()
        deck_copy = Deck.deck.copy()
        deck_played = []

        for card_a_, card_a in zip(Deck.deck, deck_copy):
            deck_played.append(card_a)
            Deck.played_card(card_a_)
            self.assertEqual(Deck.played_deck, deck_played)

