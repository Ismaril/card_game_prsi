import constants as c


def card_template(color, number):
    return f"{color}_{number}"


class Card:
    def __init__(self, card: str):
        self.__card = card
        self.__value = self.__card[2:4]
        self.__color = self.__card[0]

    def is_ace(self):
        return self.__value == c.ACE

    def is_changer(self):
        return self.__value == c.CHANGER

    def is_seven(self):
        return self.__value == c.SEVEN

    def is_non_special(self):
        return self.__value in c.NON_SPECIAL

    def is_only_color(self):
        return len(self.__card) == 1

    def is_none(self):
        """Player does not have any playable cards"""
        return self.__card == c.NONE_CARD

    def is_skipper(self):
        return self.__card == c.SKIPPER_CARD

    def card_color(self):
        return self.__color

    def card_value(self):
        return self.__value

    def get_card(self):
        """Return card"""
        return self.__card
