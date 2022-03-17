from PIL import ImageTk, Image
from functools import partial
import tkinter as tk
import sys

from hands import pc_hands, player_hands
import card


class GUI(tk.Tk):
    def __init__(self):
        # lists and set for appending gui data
        self.row_label_pc = []
        self.row_image_pc = []
        self.row_button_player = {}
        self.row_trash = []

        tk.Tk.__init__(self)
        self.grid()
        self.minsize(870, 870)
        self.title("Prší")
        self.iconbitmap("icon_heart.ico")
        self.main_grid = tk.Frame(self, bg="Green", bd=3, border=36, relief="raised", width=800, height=800)
        self.main_grid.pack(fill="both", expand=True)
        self.main_grid.grid_propagate(0)
        self.menu_bar()

        # self.start_screen()
        # self.mainloop()

    def pc_cards(self):
        """Give x cards to a pc's hand as images."""
        i = 0
        for _ in pc_hands.my_cards():
            image_pc = ImageTk.PhotoImage(Image.open("back.JPG"))
            label_card_pc = tk.Label(self.main_grid, image=image_pc)
            label_card_pc.place(relx=0.53 - (len(pc_hands.my_cards())/2*0.06) + i, rely=0.1, anchor="n")
            i += 0.06
            self.row_image_pc.append(image_pc)
            self.row_label_pc.append(label_card_pc)

    def player_cards(self):
        """Give y cards to the player's hand as images and buttons"""
        j = 0
        for y, z in enumerate(player_hands.my_cards()):
            image_player = ImageTk.PhotoImage(Image.open(f"cards_ver_1/{player_hands.my_cards()[y]}.JPG"))
            button_player = tk.Button(
                self.main_grid,
                image=image_player,
                command=partial(card.Card.get_card_players_button, y),
                text=f"{z}")
            button_player.place(relx=0.53 - (len(player_hands.my_cards())/2*0.06) + j, rely=0.9, anchor="s")
            j += 0.06
            self.row_trash.append(image_player)
            self.row_button_player.update({z: button_player})

    def middle_card(self):
        """Create image of the middle card."""
        image_middle_card = ImageTk.PhotoImage(Image.open(f"cards_ver_1/{card.middle_card.get_card()}.JPG"))
        label_middle_card = tk.Label(self.main_grid, image=image_middle_card)
        label_middle_card.place(relx=0.6, rely=0.5, anchor="center")
        self.row_trash.append(image_middle_card)
        self.row_trash.append(label_middle_card)

    def deck_card(self):
        """Create a deck image and button."""
        image_deck = ImageTk.PhotoImage(Image.open("back.JPG"))
        button_deck = tk.Button(self.main_grid, image=image_deck, command=card.Card.get_card_deck_button)
        button_deck.place(relx=0.4, rely=0.5, anchor="center")
        self.row_trash.append(image_deck)
        self.row_trash.append(button_deck)

    # create 4 buttons for changer of each color
    # def button_h(self):
    #     image_s = ImageTk.PhotoImage(Image.open("cards_ver_1/S.JPG"))
    #     button_h = tk.Button(self.main_grid, image=image_s, command=lambda: self.changer_icons("S"))
    #     button_h.place(relx=0.50, rely=0.425, anchor="center")
    #     self.row_trash.append(button_h)
    #     self.row_trash.append(image_s)
    #
    # def button_b(self):
    #     image_k = ImageTk.PhotoImage(Image.open("cards_ver_1/K.JPG"))
    #     button_b = tk.Button(self.main_grid, image=image_k, command=lambda: self.changer_icons("K"))
    #     button_b.place(relx=0.5, rely=0.475, anchor="center")
    #     self.row_trash.append(button_b)
    #     self.row_trash.append(image_k)
    #
    # def button_l(self):
    #     image_l = ImageTk.PhotoImage(Image.open("cards_ver_1/L.JPG"))
    #     button_l = tk.Button(self.main_grid, image=image_l, command=lambda: self.changer_icons("L"))
    #     button_l.place(relx=0.5, rely=0.525, anchor="center")
    #     self.row_trash.append(button_l)
    #     self.row_trash.append(image_l)
    #
    # def button_n(self):
    #     image_z = ImageTk.PhotoImage(Image.open("cards_ver_1/Z.JPG"))
    #     button_n = tk.Button(self.main_grid, image=image_z, command=lambda: self.changer_icons("Z"))
    #     button_n.place(relx=0.5, rely=0.575, anchor="center")
    #     self.row_trash.append(button_n)
    #     self.row_trash.append(image_z)

    def destroy_all_widgets(self):
        """Destroy all grid and pack slaves to free up the memory = completely delete widgets."""
        for widget in self.main_grid.place_slaves():
            widget.destroy()
        for widget in self.main_grid.grid_slaves():
            widget.destroy()

    # def start_screen(self):
    #     """Create the welcome screen."""
    #     start_frame = tk.Frame(self.main_grid, bg="Green", bd=3, border=36, width=800, height=800)
    #     start_frame.pack(fill="both", expand=True)
    #     start_frame.grid_propagate(0)
    #
    #     image_1 = ImageTk.PhotoImage(Image.open("start/b_ace.jpg"))
    #     image_1_label = tk.Label(start_frame, image=image_1, bg="green",)
    #     image_1_label.place(relx=0.05, rely=0.0, anchor="nw")
    #
    #     image_2 = ImageTk.PhotoImage(Image.open("start/n_ace.jpg"))
    #     image_2_label = tk.Label(start_frame, image=image_2, bg="green", )
    #     image_2_label.place(relx=0.95, rely=0.0, anchor="ne")
    #
    #     button_start = tk.Button(start_frame, text="PRŠÍ", bg="grey", command=start_frame.destroy)
    #     button_start.place(relx=0.5, rely=1, anchor="s", height=185, width=650)
    #     button_start.config(font=("Exo", 30, "bold"))
    #
    #     self.row_trash.append(image_1)
    #     self.row_trash.append(image_2)
    #     self.row_trash.append(image_1_label)
    #     self.row_trash.append(image_2_label)
    #     self.row_trash.append("S")

    def menu_bar(self):
        """Create the menu bar on the top left side."""
        top_menu = tk.Menu(self)
        self.config(menu=top_menu)

        game_menu = tk.Menu(top_menu, tearoff=False)
        top_menu.add_cascade(menu=game_menu, label="Menu")
        #game_menu.add_command(label="Restart", command=self.next_game)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=lambda: sys.exit())

        game_info = tk.Menu(top_menu, tearoff=False)
        top_menu.add_cascade(menu=game_info, label="Info")
        game_info.add_command(label="About", command=self.about_game)

    @staticmethod
    def about_game():
        root = tk.Tk()
        root.title("About")
        about_label = tk.Message(
            root,
            text=f"""
                {"*"*61}
                Gameplay info:
                Deck of cards is mixed at start and once it is depleted
                Both Player and PC start with 5 cards
                Order of players at the hand round is decided randomly
                Everything is executed without animation and immediately

                Product info:
                Version: 1.2
                Last update: 17.01.2022
                Technology: Python 3.X
                Creator: Tomas Laznicka 
                {"*"*61}
                """)

        about_label.pack()
        root.mainloop()

    def round_end_victory(self):
        """Round end screen - victory button."""
        game_over_frame = tk.Frame(self.main_grid, height=185, width=265)
        game_over_frame.place(relx=0.5, rely=0.8, anchor="center")
        button_victory = tk.Button(game_over_frame, text="YOU WON", bg="grey", command=self.next_round)
        button_victory.place(relx=0.5, rely=0.5, anchor="center", height=185, width=265)
        button_victory.config(font=("Exo", 30, "bold"))

    def round_end_defeat(self):
        """Round end screen - defeat button."""
        game_over_frame = tk.Frame(self.main_grid, height=185, width=265)
        game_over_frame.place(relx=0.5, rely=0.2, anchor="center")
        button_defeat = tk.Button(game_over_frame, text="YOU LOST", bg="grey", command=self.next_round)
        button_defeat.place(relx=0.5, rely=0.5, anchor="center", height=185, width=265)
        button_defeat.config(font=("Exo", 30, "bold"))

    def total_victory(self):
        """Total victory - display final screen."""
        image_victory = ImageTk.PhotoImage(Image.open("end/victory.JPG"))
        game_over_label = tk.Label(
            self.main_grid,
            width=1920,
            height=1080,
            bg="black",
            image=image_victory)
        game_over_label.place(relx=0.5, rely=0.5, anchor="center")
        self.row_trash.append(image_victory)
        self.row_trash.append(game_over_label)

    def total_defeat(self):
        """Total defeat - display final screen."""
        image_victory = ImageTk.PhotoImage(Image.open("end/death.JPG"))
        game_over_label = tk.Label(
            self.main_grid,
            width=1920,
            height=1080,
            bg="black",
            image=image_victory)
        game_over_label.place(relx=0.5, rely=0.5, anchor="center")
        self.row_trash.append(image_victory)
        self.row_trash.append(game_over_label)

    def gui_main(self):
        """Put all gui sub parts of card distribution together."""
        self.destroy_all_widgets()
        self.pc_cards()
        self.player_cards()
        self.middle_card()
        # self.deck_card()


# GUI()
