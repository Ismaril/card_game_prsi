import unittest
from card import Card, card_template
import constants as c


class TestCard(unittest.TestCase):

    def test_ace(self):
        for color in c.COLORS_ALL:
            # check if card is an ace
            card = Card(card_template(color, c.ACE))
            self.assertIs(card.is_ace(), True)

            # check if card is not an ace
            for number in c.NON_SPECIAL + [c.SEVEN] + [c.CHANGER]:
                card = Card(card_template(color, number))
                self.assertIs(card.is_ace(), False)

    def test_changer(self):
        for color in c.COLORS_ALL:
            # check if card is a changer
            card = Card(card_template(color, c.CHANGER))
            self.assertIs(card.is_changer(), True)

            # check if card is not a changer
            for number in c.NON_SPECIAL + [c.SEVEN] + [c.ACE]:
                card = Card(card_template(color, number))
                self.assertIs(card.is_changer(), False)

    def test_seven(self):
        for color in c.COLORS_ALL:
            # check if card is a seven
            card = Card(card_template(color, c.SEVEN))
            self.assertIs(card.is_seven(), True)

            # check if card is not a seven
            for number in c.NON_SPECIAL + [c.CHANGER] + [c.ACE]:
                card = Card(card_template(color, number))
                self.assertIs(card.is_seven(), False)

    def test_non_special(self):
        for color in c.COLORS_ALL:
            # check if card is not special
            for number in c.NON_SPECIAL:
                card = Card(card_template(color, number))
                self.assertIs(card.is_non_special(), True)

            # check if card is special
            for number in [c.SEVEN] + [c.CHANGER] + [c.ACE]:
                card = Card(card_template(color, number))
                self.assertIs(card.is_non_special(), False)

    def test_only_color(self):
        """Check if len() of card is only 1"""
        for color in c.COLORS_ALL:
            card = Card(color)
            self.assertIs(card.is_only_color(), True)

    def test_none_card(self):
        card = Card(c.NONE_CARD)
        self.assertIs(card.is_none(), True)

        for color in c.COLORS_ALL:
            for number in c.NUMBERS_ALL:
                card = Card(card_template(color, number))
                self.assertIs(card.is_none(), False)

    def test_skipper(self):
        card = Card(c.SKIPPER_CARD)
        self.assertIs(card.is_skipper(), True)

        for color in c.COLORS_ALL:
            for number in c.NUMBERS_ALL:
                card = Card(card_template(color, number))
                self.assertIs(card.is_skipper(), False)

    def test_color(self):
        for color in c.COLORS_ALL:
            for number in c.NUMBERS_ALL:
                card = Card(card_template(color, number))
                self.assertEqual(card.card_color(), color)

    def test_value(self):
        for color in c.COLORS_ALL:
            for number in c.NUMBERS_ALL:
                card = Card(card_template(color, number))
                self.assertEqual(card.card_value(), number)

    def test_get_card(self):
        for color in c.COLORS_ALL:
            for number in c.NUMBERS_ALL:
                card = Card(card_template(color, number))
                self.assertEqual(card.get_card(),
                                 card_template(color, number))