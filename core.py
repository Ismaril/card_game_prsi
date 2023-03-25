from deck import Deck
from card import Card
from hands import Hands
from functools import partial
from PIL import ImageTk, Image
import sys
import os.path
import random as r
import tkinter as tk
import constants as c


class GUI(tk.Tk):
    def __init__(self):
        self.row_label_pc = []
        self.row_image_pc = []
        self.row_button_player = {}
        self.row_rest = []
        self.start_frame = []
        self.GUI_drawn = False

        tk.Tk.__init__(self)
        self.grid()
        self.minsize(870, 870)
        self.title("Prší")
        self.iconbitmap("icon_heart.ico")
        self.main_grid = tk.Frame(
            self,
            bg=c.BACKROUND_COLOR,
            bd=3,
            border=36,
            relief="raised",
            width=c.FRAME_SIZE,
            height=c.FRAME_SIZE
        )
        self.main_grid.pack(fill="both", expand=True)
        self.main_grid.grid_propagate(0)
        self.__menu_bar()

    def __pc_cards(self):
        """Give x cards to a pc's hand as images."""
        distance = 0
        for _ in Logic.pc_hands.my_cards():
            image = ImageTk.PhotoImage(Image.open(c.CARD_STYLE_BACK + ".JPG"))
            label = tk.Label(self.main_grid, image=image)
            label.place(
                relx=c.MIDDLE_POS_HANDS - (
                        len(Logic.pc_hands.my_cards()) / 2 * c.DIST_BETWEEN_CARDS) + distance,
                rely=c.RELY_PC_CARDS,
                anchor="n"
            )
            distance += c.DIST_BETWEEN_CARDS
            self.row_image_pc.append(image)
            self.row_label_pc.append(label)

    def __player_cards(self):
        """Give y cards to the player's hand as images and buttons"""
        distance = 0
        for index, card in enumerate(Logic.player_hands.my_cards()):
            image = ImageTk.PhotoImage(
                Image.open(f"{c.CARD_STYLE_FRONT}/{card}.JPG"))
            button = tk.Button(
                self.main_grid,
                image=image,
                command=partial(Logic.name_of_card, index),
                text=f"{card}"
            )
            button.place(
                relx=c.MIDDLE_POS_HANDS - (
                        len(Logic.player_hands.my_cards()) / 2 * c.DIST_BETWEEN_CARDS) + distance,
                rely=c.RELY_PLAYER_CARDS,
                anchor="s"
            )
            distance += c.DIST_BETWEEN_CARDS
            self.row_rest.append(image)
            self.row_button_player.update({card: button})

    def __middle_card(self):
        """Create image of the middle card."""
        image = ImageTk.PhotoImage(
            Image.open(
                f"{c.CARD_STYLE_FRONT}/{Logic.middle_card.get_card()}.JPG"))
        label = tk.Label(self.main_grid, image=image)
        label.place(relx=c.RELY_PLAYED_CARD, rely=c.WIDGET_MIDDLE,
                    anchor="center")
        self.row_rest.append(image)
        self.row_rest.append(label)

    def __deck_card(self):
        """Create a deck image and button."""
        image = ImageTk.PhotoImage(Image.open(c.CARD_STYLE_BACK + ".JPG"))
        button = tk.Button(self.main_grid, image=image,
                           command=Logic.get_card_deck_button)
        button.place(relx=c.RELY_DECK_CARD, rely=c.WIDGET_MIDDLE,
                     anchor="center")
        self.row_rest.append(image)
        self.row_rest.append(button)

    def changer_icons_(self):
        """Create icons of 4 colors when playing any changer"""
        if Logic.changer_buttons \
                and len(Logic.player_hands.my_cards()) >= 1:
            rely = c.RELY_CHANGER_ICONS_BASE
            for color in c.COLORS_ALL:
                image = ImageTk.PhotoImage(
                    Image.open(
                        os.path.join(c.CARD_STYLE_FRONT, f"{color}.JPG")))
                button = tk.Button(
                    self.main_grid,
                    image=image,
                    command=partial(Logic.changer_icons, color)
                )
                button.place(relx=c.WIDGET_MIDDLE, rely=rely, anchor="center")
                rely += c.RELY_CHANGER_ICONS
                self.row_rest.append(image)
                self.row_rest.append(button)

    def __destroy_all_widgets(self):
        """Destroy all grid and pack slaves = completely delete widgets."""
        # TODO: delete only widgets that have to be deleted at a given time
        for widget in self.main_grid.place_slaves():
            widget.destroy()
        for widget in self.main_grid.grid_slaves():
            widget.destroy()

    def start_screen(self):
        """Create the welcome screen."""
        if not Logic.start_screen:
            frame = tk.Frame(self.main_grid, bg=c.BACKROUND_COLOR, bd=3,
                             border=36, width=c.FRAME_SIZE,
                             height=c.FRAME_SIZE)
            frame.pack(fill="both", expand=True)
            frame.grid_propagate(0)

            image_1 = ImageTk.PhotoImage(Image.open(c.WELCOME_SCREEN_CARD_1))
            image_1_label = tk.Label(frame, image=image_1,
                                     bg=c.BACKROUND_COLOR, )
            image_1_label.place(relx=0.05, rely=0.0, anchor="nw")
            image_2 = ImageTk.PhotoImage(Image.open(c.WELCOME_SCREEN_CARD_2))
            image_2_label = tk.Label(frame, image=image_2,
                                     bg=c.BACKROUND_COLOR, )
            image_2_label.place(relx=0.95, rely=0.0, anchor="ne")

            self.row_rest.extend([image_1, image_2])
            self.row_rest.extend([image_1_label, image_2_label])

            # condition for different style of cards
            if not c.CARD_STYLE:
                image_3 = ImageTk.PhotoImage(
                    Image.open(c.WELCOME_SCREEN_CARD_3))
                image_3_label = tk.Label(frame, image=image_3,
                                         bg=c.BACKROUND_COLOR, )
                image_3_label.place(relx=0.05, rely=1.0, anchor="sw")
                image_4 = ImageTk.PhotoImage(
                    Image.open(c.WELCOME_SCREEN_CARD_4))
                image_4_label = tk.Label(frame, image=image_4,
                                         bg=c.BACKROUND_COLOR, )
                image_4_label.place(relx=0.95, rely=1.0, anchor="se")
                self.row_rest.extend([image_3, image_4])
                self.row_rest.extend([image_3_label, image_4_label])

            self.start_frame.append(frame)

    @staticmethod
    def __change_style_of_cards(users_pick):
        """Write down into file type of cardstyle, which will result
        in change of card style drawn on the screen"""
        with open("user_settings.txt", "r") as file:
            background_settings = file.readline()[1]
        with open("user_settings.txt", "w") as file:
            file.write(f"{users_pick}{background_settings}")

    @staticmethod
    def __change_style_of_gui_background(users_pick):
        """Write down into file type of background, which will result
        in change of gui background"""
        with open("user_settings.txt", "r") as file:
            card_settings = file.readline()[0]
        with open("user_settings.txt", "w") as file:
            file.write(f"{card_settings}{users_pick}")

    def __menu_bar(self):
        """Create the menu bar on the top left side."""
        top_menu = tk.Menu(self)
        self.config(menu=top_menu)

        game_menu = tk.Menu(top_menu, tearoff=False)
        top_menu.add_cascade(menu=game_menu, label="Menu")
        game_menu.add_command(label="Restart (Restarts the game)",
                              command=lambda: Logic.next_game())
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=lambda: sys.exit())

        settings = tk.Menu(top_menu, tearoff=False)
        top_menu.add_cascade(menu=settings, label="Settings")
        settings.add_command(label="Changes below require restart of program")
        settings.add_separator()
        settings.add_command(
            label="Card style - Poker",
            command=partial(self.__change_style_of_cards, 0))
        settings.add_command(
            label="Card style - Bavarian",
            command=partial(self.__change_style_of_cards, 1))
        settings.add_command(
            label="Background - Green",
            command=partial(self.__change_style_of_gui_background, 0))
        settings.add_command(
            label="Background - Blue",
            command=partial(self.__change_style_of_gui_background, 1))
        settings.add_command(
            label="Background - Red",
            command=partial(self.__change_style_of_gui_background, 2))
        settings.add_command(
            label="Background - Black",
            command=partial(self.__change_style_of_gui_background, 3))

        game_info = tk.Menu(top_menu, tearoff=False)
        top_menu.add_cascade(menu=game_info, label="Info")
        game_info.add_command(
            label="""T.Laznicka, Python 3.10, V2.1, 25.03.2023""")

    def round_end_screen(self):
        """Round end screen - next round button."""
        if not Logic.pc_hands.my_cards() or not Logic.player_hands.my_cards():
            rely = 0.8 if not Logic.player_hands.my_cards() else 0.2
            text = "YOU WON" if not Logic.player_hands.my_cards() else "YOU LOST"

            frame = tk.Frame(self.main_grid, height=185, width=265)
            frame.place(relx=c.WIDGET_MIDDLE, rely=rely, anchor="center")
            button = tk.Button(
                frame,
                text=text,
                bg="grey",
                command=Logic.next_game
            )
            button.place(
                relx=c.WIDGET_MIDDLE,
                rely=c.WIDGET_MIDDLE,
                anchor="center",
                height=185,
                width=265
            )
            button.config(font=("Exo", 30, "bold"))

    def total_end_screen(self):
        """Total end - display final screen."""
        if not Logic.pc_nr_cards or not Logic.player_nr_cards:
            img = "end/victory.JPG" if not Logic.player_hands.my_cards() else "end/death.JPG"

            image = ImageTk.PhotoImage(Image.open(img))
            label = tk.Label(
                self.main_grid,
                width=1920,
                height=1080,
                bg="black",
                image=image
            )
            label.place(relx=c.WIDGET_MIDDLE, rely=c.WIDGET_MIDDLE,
                        anchor="center")
            self.row_rest.append(image)
            self.row_rest.append(label)

    def gui_main(self):
        """Put all gui sub parts of card distribution together."""
        if not Logic.total_game_ended:
            self.__destroy_all_widgets()
            self.__pc_cards()
            self.__player_cards()
            self.__middle_card()
            self.__deck_card()
            self.GUI_drawn = True


class Logic:
    start_screen = False
    game_started = False
    hand_round_ = False
    pc_turn = r.choice([True, False])
    player_turn = not pc_turn
    player_interaction = False
    game_ended = False
    total_game_ended = False
    changer_buttons = False
    pc_hands = Hands("")
    player_hands = Hands("")
    middle_card = Card(" ")
    players_choice = Card(" ")
    past_players_nr_of_cards = c.STARTER_COUNT
    past_pc_nr_of_cards = c.STARTER_COUNT
    pc_nr_cards = c.STARTER_COUNT
    player_nr_cards = c.STARTER_COUNT
    seven_penalty = 0
    past_round = 1
    current_round = 1
    gui = GUI()

    @classmethod
    def hand_round(cls):
        """Distribute cards between players, start of a round."""
        if not cls.hand_round_:
            cls.gui.start_frame[0].destroy()
            Deck.create_deck()
            Deck.deck_shuffle()

            for _ in range(cls.pc_nr_cards):
                cls.pc_hands.add_new_card()
            for _ in range(cls.player_nr_cards):
                cls.player_hands.add_new_card()

            cls.middle_card = Card(Deck.deck[0])
            Deck.played_deck.append(Deck.deck[0])
            del Deck.deck[0]

            if cls.middle_card.is_ace():
                if cls.pc_turn:
                    cls.player_turn = True
                    cls.pc_turn = False
                elif cls.player_turn:
                    cls.player_turn = False
                    cls.pc_turn = True
            elif cls.middle_card.is_changer():
                cls.middle_card = Card(r.choice(c.COLORS_ALL))
            elif cls.middle_card.is_seven():
                cls.seven_penalty += 2

            cls.game_started = True
            cls.hand_round_ = True

    @classmethod
    def logic_pc(cls):
        """Logic of a pc based on it's current hand list."""
        if not cls.game_ended and cls.pc_turn:
            color = cls.middle_card.card_color()
            value = cls.middle_card.card_value()
            aces = Hands.best_pick(
                cls.pc_hands.aces(),
                color=color,
                value=value
            )
            sevens = Hands.best_pick(
                cls.pc_hands.sevens(),
                color=color,
                value=value
            )
            non_special = Hands.best_pick(
                cls.pc_hands.non_special_cards(),
                color=color,
                value=value
            )
            changers = cls.pc_hands.changers()
            aces_player = cls.player_hands.aces()

            if not non_special and not aces and not changers and not sevens:
                if cls.middle_card.is_seven() and cls.seven_penalty:
                    cls.out_of_deck()
                    for x in range(cls.seven_penalty):
                        cls.pc_hands.add_new_card()
                    cls.seven_penalty = 0
                else:
                    cls.pc_hands.add_new_card()
                    if cls.middle_card.is_ace():
                        cls.pc_turn = False
                        cls.player_turn = True

            elif cls.middle_card.is_seven() and not sevens and cls.seven_penalty:
                cls.out_of_deck()
                for x in range(cls.seven_penalty):
                    cls.pc_hands.add_new_card()
                cls.seven_penalty = 0

            elif cls.player_hands.last_card() and cls.middle_card.is_only_color() and changers:
                # when player is changing color and has only 1 card left, pc
                # below checks if can change the color to prevent the player's
                # victory
                if Hands(
                        cls.pc_hands.my_cards()).most_frequent_color() == cls.middle_card.card_color():
                    x = Card(Hands(
                        cls.pc_hands.my_cards()).second_most_frequent_color())
                    if isinstance(x, list):
                        x.remove(cls.middle_card.card_color())
                        cls.middle_card = r.choice(x)
                    else:
                        cls.middle_card = x
                else:
                    cls.middle_card = Card(
                        Hands(cls.pc_hands.my_cards()).most_frequent_color())
                cls.pc_hands.remove_card(changers[0])

            elif aces and aces_player and not cls.seven_penalty:
                cls.middle_card = Card(aces[0])
                cls.pc_hands.remove_card(aces[0])

            elif aces and not cls.seven_penalty:
                cls.middle_card = Card(aces[0])
                cls.pc_hands.remove_card(aces[0])

            elif sevens:
                cls.seven_penalty += 2
                cls.middle_card = Card(sevens[0])
                cls.pc_hands.remove_card(sevens[0])

            elif non_special:
                cls.middle_card = Card(non_special[0])
                cls.pc_hands.remove_card(non_special[0])

            elif changers and not non_special:
                cls.middle_card = Card(
                    Hands(cls.pc_hands.my_cards()).most_frequent_color())
                cls.pc_hands.remove_card(changers[0])

            if cls.middle_card.is_ace() and not cls.player_hands.aces():
                # pc plays again due to ace
                return
            else:
                cls.pc_turn = False
                cls.player_turn = True

    @classmethod
    def logic_player(cls):
        """Logic of the player based on his current hand list."""
        if not cls.game_ended and cls.player_turn and cls.player_interaction:
            if cls.middle_card.is_seven() and cls.seven_penalty and not cls.player_hands.sevens():
                cls.out_of_deck()
                for x in range(cls.seven_penalty):
                    cls.player_hands.add_new_card()
                cls.seven_penalty = 0

            elif cls.players_choice.is_none():
                cls.player_hands.add_new_card()

            elif cls.players_choice.is_changer() and not cls.seven_penalty:
                cls.changer_buttons = True
                cls.middle_card = cls.players_choice
                cls.player_hands.remove_card(cls.players_choice.get_card())
                cls.players_choice = Card("_")

            elif cls.middle_card.card_color() \
                    in cls.players_choice.get_card() \
                    or cls.middle_card.card_value() \
                    in cls.players_choice.get_card():

                if cls.players_choice.is_ace() and cls.pc_hands.aces():
                    cls.middle_card = cls.players_choice
                    cls.player_hands.remove_card(cls.players_choice.get_card())

                elif cls.players_choice.is_ace():
                    cls.middle_card = cls.players_choice
                    cls.player_hands.remove_card(cls.players_choice.get_card())
                    cls.players_choice = Card("_")

                elif cls.players_choice.is_seven():
                    cls.middle_card = cls.players_choice
                    cls.player_hands.remove_card(cls.players_choice.get_card())
                    cls.seven_penalty += 2

                else:
                    if cls.players_choice.is_skipper():
                        pass
                    # player plays non special card
                    else:
                        cls.middle_card = cls.players_choice
                        cls.player_hands.remove_card(
                            cls.players_choice.get_card())

            if cls.players_choice.is_skipper():
                # skip code if playing a changer or an ace (due to loop)
                return
            else:
                cls.pc_turn = True
                cls.player_turn = False
                cls.player_interaction = False

    @classmethod
    def name_of_card(cls, index):
        """Get a name of card based on the player's button choice"""
        card_n = Card(Logic.player_hands.my_cards()[index])

        # filter cards that must not be put on the middle card
        if (cls.middle_card.is_ace()
            and not card_n.is_ace()
            and cls.player_hands.aces()) \
                or cls.middle_card.is_changer():
            return

        elif (
                card_n.is_changer() and not card_n.is_seven() and not cls.seven_penalty) \
 \
                or ((card_n.card_color() in cls.middle_card.get_card()
                     or card_n.card_value() in cls.middle_card.get_card())
                    and not card_n.is_changer()
                    and not cls.seven_penalty) \
 \
                or (card_n.is_seven() and cls.middle_card.is_seven()):

            cls.players_choice = card_n
            cls.player_interaction = True

        else:
            return

    @classmethod
    def get_card_deck_button(cls):
        """Get another card from the deck when the deck button is pressed."""
        if cls.game_ended \
                or cls.middle_card.is_changer() \
                or (cls.middle_card.is_ace() and cls.player_hands.aces()) \
                or (cls.middle_card.is_seven() and cls.player_hands.sevens()):
            return
        else:
            cls.players_choice = Card("n")
            cls.player_interaction = True

    @classmethod
    def next_game(cls):
        """
        Play the game again with 5 vs 5 cards
        OR
        Play next round if round has ended.
        """
        if cls.game_ended:
            if not cls.player_hands.my_cards():
                cls.pc_nr_cards += 1
                cls.player_nr_cards -= 1
            elif not cls.pc_hands.my_cards():
                cls.pc_nr_cards -= 1
                cls.player_nr_cards += 1

        elif not cls.game_ended:
            cls.pc_nr_cards = c.STARTER_COUNT
            cls.player_nr_cards = c.STARTER_COUNT

        cls.past_players_nr_of_cards = cls.player_nr_cards
        cls.past_pc_nr_of_cards = cls.pc_nr_cards
        cls.pc_hands.my_cards().clear()
        cls.player_hands.my_cards().clear()
        cls.game_started = False
        cls.game_ended = False
        cls.total_game_ended = False
        cls.hand_round_ = False
        cls.player_interaction = False
        cls.changer_buttons = False
        cls.pc_turn = r.choice([True, False])
        cls.player_turn = not cls.pc_turn
        cls.pc_hands = Hands("")
        cls.player_hands = Hands("")
        cls.middle_card = Card(" ")
        cls.players_choice = Card(" ")
        cls.seven_penalty = 0
        cls.current_round += 1
        Deck.clear_deck()

    @classmethod
    def check_the_status(cls):
        """Check who is the winner"""
        if not cls.pc_nr_cards or not cls.player_nr_cards:
            cls.total_game_ended = True
        elif not cls.pc_hands.my_cards() or not cls.player_hands.my_cards():
            cls.game_ended = True

    @classmethod
    def out_of_deck(cls):
        """
        Mix played cards and append them to the deck.
        """
        # if all cards together and debt of sevens exceed remaining cards
        # in deck, append played cards to the deck sooner
        if (len(Deck.played_deck)
            + len(cls.pc_hands.my_cards())
            + len(cls.player_hands.my_cards())
            == 32) \
                or (len(Deck.played_deck)
                    + len(cls.pc_hands.my_cards())
                    + len(cls.player_hands.my_cards())
                    + cls.seven_penalty
                    > 32):
            last_card_out = Deck.played_deck.pop()
            Deck.deck_shuffle()
            Deck.put_deck_cards_together()
            Deck.played_deck.append(last_card_out)

    @classmethod
    def changer_icons(cls, letter):
        """Change the middle card to 'color only' when played a changer."""
        cls.middle_card = Card(letter)
        cls.pc_turn = True
        cls.player_turn = False
        cls.changer_buttons = False
        cls.gui.gui_main()
