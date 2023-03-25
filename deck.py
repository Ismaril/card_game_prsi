import random
import constants as c
from card import card_template


class Deck:
    """Deck containing 32 cards divided into 4 colors"""
    deck = []
    played_deck = []

    @staticmethod
    def create_deck():
        for color in c.COLORS_ALL:
            for value in c.NUMBERS_ALL:
                Deck.deck.append(card_template(color, value))

    @staticmethod
    def deck_shuffle():
        random.shuffle(Deck.deck)

    @staticmethod
    def put_deck_cards_together():
        """Extend deck by played deck"""
        Deck.deck.extend(Deck.played_deck)
        Deck.played_deck.clear()

    @staticmethod
    def take_next_card():
        """Take next card and remove it from deck"""
        return Deck.deck.pop(0)

    @staticmethod
    def played_card(card):
        """Put current played card into played deck"""
        Deck.played_deck.append(card)

    @staticmethod
    def clear_deck():
        """Remove contents of deck"""
        Deck.deck.clear()
        Deck.played_deck.clear()
