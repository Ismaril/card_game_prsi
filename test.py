import constants as c
from card import card_template
from core import Logic
from deck import Deck


def __test_card_composition(player_hands: list,
                            pc_hands: list,
                            deck: list,
                            played_deck: list):
    """
    Test card composition during runtime.
    Check if all cards match the 4 colors and having 8 cards each.

    :param player_hands:
    :param pc_hands:
    :param deck:
    :param played_deck:
    :return:
    """
    deck_true = []
    for color in c.COLORS_ALL:
        for value in c.NUMBERS_ALL:
            deck_true.append(card_template(color, value))
    deck_true.sort()

    deck_runtime = player_hands + pc_hands + deck + played_deck
    deck_runtime.sort()

    return deck_true == deck_runtime


def runtime_test(verbose=False):
    assert __test_card_composition(Logic.player_hands.my_cards(),
                                   Logic.pc_hands.my_cards(),
                                   Deck.deck,
                                   Deck.played_deck), \
        f"The cards in circulation during runtime deviate from specification.\n" \
        f"Player's hands: {Logic.player_hands.my_cards()}\n" \
        f"PC's hands: {Logic.pc_hands.my_cards()}\n" \
        f"Deck: {sorted(Deck.deck)}\n" \
        f"Played deck: {sorted(Deck.played_deck)}\n"

    if verbose:
        print("pc", Logic.pc_hands.my_cards())
        print("middle", Logic.middle_card.get_card())
        print("player", Logic.player_hands.my_cards())
