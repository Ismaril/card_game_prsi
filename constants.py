from os import path

# CARD TYPES
NUMBERS_ALL = ["07", "08", "09", "10", "11", "12", "13", "14"]
ACE = NUMBERS_ALL[-1]
CHANGER = NUMBERS_ALL[5]
SEVEN = NUMBERS_ALL[0]
NON_SPECIAL = NUMBERS_ALL[1:5] + [NUMBERS_ALL[-2]]
NONE_CARD = 'n'
SKIPPER_CARD = '_'
COLORS_ALL = ["L", "B", "N", "H"]  # [Leaves, Ballz, Nuts, Hearths]

# PATHS
CARD_STYLES_FRONT = "card_styles"
CARD_STYLES_BACK = path.join(CARD_STYLES_FRONT, "styles_back")

# STYLES OF CARDS DRAWN AT THE SCREEN
try:
    with open("user_settings.txt", "r") as file:
        users_style_pick = int(file.read())
except FileNotFoundError as error:
    print(error, "Exception handled")
    users_style_pick = 0

CARD_STYLE_FRONT_OPTIONS = ("poker_style_front", "bavarian_style_front")
CARD_STYLE_BACK_OPTIONS = ("poker_blue", "bavarian_black")
CARD_STYLE_FRONT = path.join(CARD_STYLES_FRONT,
                             CARD_STYLE_FRONT_OPTIONS[users_style_pick])
CARD_STYLE_BACK = path.join(CARD_STYLES_BACK,
                            CARD_STYLE_BACK_OPTIONS[users_style_pick])

# ADJUST REL COORDINATES BASED ON SIZE OF CARDS
match users_style_pick:
    case 0:
        RELY_PC_CARDS = 0.02
        RELY_PLAYER_CARDS = 0.98
        WELCOME_SCREEN_CARD_1 = path.join(CARD_STYLE_FRONT, "B_13.jpg")
        WELCOME_SCREEN_CARD_2 = path.join(CARD_STYLE_FRONT, "H_13.jpg")
        WELCOME_SCREEN_CARD_3 = path.join(CARD_STYLE_FRONT, "N_13.jpg")
        WELCOME_SCREEN_CARD_4 = path.join(CARD_STYLE_FRONT, "L_13.jpg")
        RELY_DECK_CARD = 0.3
        RELY_PLAYED_CARD = 0.7
        RELY_CHANGER_ICONS = 0.065
        RELY_CHANGER_ICONS_BASE = 0.40

    case 1:
        RELY_PC_CARDS = 0.1
        RELY_PLAYER_CARDS = 0.9
        WELCOME_SCREEN_CARD_1 = "start/B_ACE_HQ.jpg"
        WELCOME_SCREEN_CARD_2 = "start/H_ACE_HQ.jpg"
        RELY_DECK_CARD = 0.4
        RELY_PLAYED_CARD = 0.6
        RELY_CHANGER_ICONS = 0.05
        RELY_CHANGER_ICONS_BASE = 0.425

# STYLE OF BACKGROUND
BACKROUND_COLOR = "green"

# INITIAL NUMBER OF CARDS FOR EACH PLAYER
STARTER_COUNT = 5

# GENERAL GUI CONSTANTS
DIST_BETWEEN_CARDS = 0.06
MIDDLE_POS_HANDS = 0.53
WIDGET_MIDDLE = 0.5
FRAME_SIZE = 800

