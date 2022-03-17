import random


class Deck:
    """Deck containing 32 cards divided into 4 colors"""
    __colors = ["L", "B", "N", "H"]  # [Leaves, Ballz, Nuts, Hearths]
    __values = range(7, 15)
    deck = []
    played_deck = []

    for color in __colors:
        for value in __values:
            if value in range(10, 15):
                deck.append(f"{color}_{value}")
            else:
                deck.append(f"{color}_0{value}")

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
