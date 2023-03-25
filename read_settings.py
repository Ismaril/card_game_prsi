def read_settings_():
    """
    Read from text file the settings of cardstyles and background color of gui.

    :return: int, int
    """
    try:
        with open("user_settings.txt", "r") as file:
            complete_string = file.read()
            card_style = int(complete_string[0])
            background_style = int(complete_string[1])

    except (FileNotFoundError, IndexError) as error:
        print(error, "Exception handled")
        card_style = 0
        background_style = 0

    return card_style, background_style
