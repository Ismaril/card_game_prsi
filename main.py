import time

import constants
from core import Logic
from test import runtime_test, runtime_monitoring

GUI = Logic.gui


def master_mainloop():
    Logic.hand_round()

    Logic.logic_pc()
    Logic.logic_player()
    Logic.out_of_deck()
    Logic.check_the_status()
    runtime_test()

    # Redraw screen only when there is some change during game.
    if Logic.past_players_nr_of_cards != len(Logic.player_hands.my_cards()) \
            or Logic.past_pc_nr_of_cards != len(Logic.pc_hands.my_cards()) \
            or Logic.past_round != Logic.current_round \
            or not GUI.is_GUI_drawn:
        if Logic.past_round != Logic.current_round:
            Logic.past_round += 1
        Logic.past_players_nr_of_cards = len(Logic.player_hands.my_cards())
        Logic.past_pc_nr_of_cards = len(Logic.pc_hands.my_cards())
        GUI.gui_main()
        GUI.changer_icons_()
        GUI.round_end_screen()
        GUI.total_end_screen()
        runtime_monitoring(verbose=True)

    milliseconds = constants.DELAY_PLAYER if Logic.is_player_turn else constants.DELAY_PC
    GUI.after(milliseconds, master_mainloop)  # run again after X ms


if __name__ == "__main__":
    GUI.start_screen()
    GUI.after(000, master_mainloop)  # run first time after X ms
    GUI.mainloop()

# TODO: sometimes there is a bug where pc plays a seven, two
#   cards are automatically assigned to player from deck and still
#   it is players turn.
# TODO: flickering was largely removed but still happens from time to time.
#  Destroy only specific widgets at a time, not all.
# TODO: make a log of every game, written into txt, for debugging reasons

