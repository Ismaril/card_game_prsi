

class Card:
    def __init__(self, card: str):
        self.__card = card
        self.__value = self.__card[2:4]
        self.__color = self.__card[0]

    def is_ace(self):
        return self.__value == "14"

    def is_changer(self):
        return self.__value == "12"

    def is_seven(self):
        return self.__value == "07"

    def is_non_special(self):
        return self.__value in ["08", "09", "10", "11", "13"]

    def is_only_color(self):
        return len(self.__card) == 1

    def is_none(self):
        """Player does not have any playable cards"""
        return self.__card == "n"

    def is_skipper(self):
        return self.__card == "_"

    def card_color(self):
        return self.__color

    def card_value(self):
        return self.__value

    def get_card(self):
        """Return card"""
        return self.__card

