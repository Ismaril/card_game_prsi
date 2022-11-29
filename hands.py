from deck import Deck
from collections import Counter
import constants as c

class Hands:
    """Hand of player containing cards"""
    def __init__(self, cards):
        self.__cards = cards if isinstance(cards, list) else list(cards)

    def my_cards(self):
        return self.__cards

    def last_card(self):
        return len(self.__cards) == 1

    def add_new_card(self):
        self.__cards.append(Deck.take_next_card())

    def remove_card(self, card_to_remove):
        card_to_remove = self.__cards.pop(self.__cards.index(card_to_remove))
        Deck.played_card(card_to_remove)

    def aces(self):
        return [card for card in self.__cards if card.endswith(c.ACE)]

    def changers(self):
        return [card for card in self.__cards if card.endswith(c.CHANGER)]

    def sevens(self):
        return [card for card in self.__cards if card.endswith(c.SEVEN)]

    def non_special_cards(self):
        return [y for y in self.__cards if
                not y.endswith(c.SEVEN)
                and not y.endswith(c.CHANGER)
                and not y.endswith(c.ACE)]

    @staticmethod
    def best_pick(array, color, value):
        """Filter out card that does not match color or value"""
        res = []
        for y in array:
            if color and value:
                if y.startswith(color) or y.endswith(value):
                    res.append(y)
            elif color:
                if y.startswith(color):
                    res.append(y)
        return res

    def most_freq(self):
        """Find most frequent color when playing a changer"""
        if len(self.__cards) == len(self.changers()):
            return self.__cards[0][0]
        else:
            data = Counter([y[0] for y in self.my_cards() if not y.endswith(c.CHANGER)])
            most_common = data.most_common()[0][0]
            return most_common

    def second_most_freq(self):
        """Find second most frequent color when playing a changer"""
        if len(self.__cards) == len(self.changers()):
            return Deck.colors
        else:
            data = Counter([y[0] for y in self.__cards if not y.endswith(c.CHANGER)])
            if len(data.most_common()) == 1:
                return Deck.colors
            else:
                second_most_common = data.most_common()[1][0]
                return second_most_common

