from core import Logic

GUI = Logic.gui


def master_mainloop():
    Logic.hand_round()
    Logic.logic_pc()
    Logic.logic_player()
    Logic.out_of_deck()
    Logic.check_the_status()
    GUI.gui_main()
    GUI.changer_icons_()
    GUI.round_end_screen()
    GUI.total_end_screen()
    GUI.after(2000, master_mainloop)  # run again after X ms


if __name__ == "__main__":
    GUI.start_screen()
    GUI.after(4000, master_mainloop)  # run first time after X ms
    GUI.mainloop()
