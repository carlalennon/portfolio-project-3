# Get narrative from run.py
from narrative import get_narrative_dict
from choice import get_choice_dict

narrative_dict = get_narrative_dict()
choice_dict = get_choice_dict()

# Player setup to hold status effects and name
class Player:
    def __init__(self):
        self.name = ''
        self.time = ''
        self.room = ''
        self.score = ''
        self.stage = 0
        self.branch = ''
        self.gameover = ''


you = Player()


def title_screen():
    print("################")
    print("# Closing Time #")
    print("################")
    print("#     PLAY     #")
    print("#     ABOUT    #")
    title_screen_selections()


# Title screen
def title_screen_selections():
    option = input("> \n")
    if option.lower() == "play":
        start_game()
    elif option.lower() == "about":
        about_game()
    while option.lower() not in ["play", "about", "quit"]:
        print("please enter a valid option")
        option = input("> \n")
        if option.lower() == "play":
            start_game()
        elif option.lower() == "about":
            about_game()


def about_game():
    print("Made in 2023")
    print("Characters:")
    print("Sean : The owner of the pub and")
    print("      a big softie.")
    print("Tomas : A strange man with a lot")
    print("       to say.")
    print("Mairead : A woman who loves nothing")
    print("         more than to gamble, except")
    print("         maybe her violent son.")
    print("Type back to exit to menu")
    back = input("> \n")
    if back.lower() == "back":
        title_screen()
    else:
        print("Type back to exit to menu")
        back = input("> \n")


# Logic
def start_game():
    Player.room = "porch"  # sets player room
    Player.score = 0
    Player.stage = 0
    Player.gameover = False
    get_name()


def get_name():
    question_name = "What is your name?\n"
    print(question_name)
    player_name = input("> \n")
    Player.name = player_name
    set_player_ui()
    rules()


def rules():
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    print("\n Weclome, " + Player.name + ".")
    print("Try not to get thrown out of the pub")
    print("or be forced to leave before midnight.")
    print("Choose you path by typing the text")
    print("within the [Brackets].")
    print("Make good choices...\n")
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    player_input_branch_definition()


def set_player_ui():
    Player.time = 0
    Player.room = "  "


def game_over():
    if choice_dict[Player.stage] == "GAME OVER":
        Player.gameover = True
        game_over_message()
    else:
        Player.gameover = False
        game_loop()


def game_loop():
    room()  # Prints room plater is in
    time_increment()  # Adds 1hour to each turn
    time()  # Prints time
    score_add()  # Adds score
    score()  # Prints score
    narrative()  # Prints narrative values
    player_answer()


# Player information
def room():
    """
    Prints the room the player is in (Indicates branch)
    """
    player_room = choice_dict[Player.stage]["room"]
    if Player.room:
        print("--Current room: ------------")
        print("\n" + player_room.upper())
        print("----------------------------")
    else:
        print("roomError")


def time_increment():
    Player.time = Player.time + 1


def time():
    if Player.time == 0:
        print("20:00")
    elif Player.time == 1:
        print("21:00")
    elif Player.time == 2:
        print("22:00")
    elif Player.time == 3:
        print("23:00")
    elif Player.time == 4:
        print("00:00")
    elif Player.time == 5:
        print("01:00")
    elif Player.time == 6:
        print("02:00")
    elif Player.time == 7:
        print("03:00")
    else:
        print("TimeError")


def score_add():
    if Player.stage in choice_dict:
        Player.score += choice_dict[Player.stage]["Win"]["Score"]
    else:
        return


def score():
    print("Score: " + str(Player.score))


def narrative():
    if Player.stage == 0:
        player_input_branch_definition()
    else:
        print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
        for value in narrative_dict[Player.stage].values():
            print(value)
        print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")


def player_answer():
    if choice_dict[Player.stage] != "GAME OVER":
        print("\n Enter your choice below:")
        choice = input("> \n")
        win = choice_dict[Player.stage]["Win"]["Choice"]
        lose = choice_dict[Player.stage]["Lose"]["Choice"]
        if choice.lower() not in [win, lose]:
            print("Please enter a valid choice")
        if choice.lower() == win:
            flavour_print_win()
        elif choice.lower() == lose:
            flavour_print_lose()
    return


def game_over_message():
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    for value in narrative_dict[Player.stage].values():
        print(value)
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    return


def flavour_print_win():
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    for value in choice_dict[Player.stage]["Win"]["Flavour"].values():
        print(value)
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    narrative = choice_dict[Player.stage]["Win"]["narrative"]
    Player.stage = narrative
    game_over()


def flavour_print_lose():
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    for value in choice_dict[Player.stage]["Lose"]["Flavour"].values():
        print(value)
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    narrative = choice_dict[Player.stage]["Lose"]["narrative"]
    Player.stage = narrative
    game_over()


def player_input_branch_definition():
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    for value in narrative_dict[Player.stage].values():
        print(value)
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    action = input("> \n")
    valid_actions = ["gamble", "pool table", "sean", "tomas", "birthday party"]
    while action.lower() not in valid_actions:
        print("Please enter a valid action. \n")
        action = input("> \n")
    if action.lower() == "gamble":
        define_branch_fruit()
    elif action.lower() == "pool table":
        define_branch_pool()
    elif action.lower() == "sean":
        define_branch_sean()
    else:
        print("Please enter a valid option")
        action = input("> \n")


def define_branch_fruit():
    Player.room = "fruit machine"
    Player.stage = 1
    game_loop()


def define_branch_pool():
    Player.room = "pool table"
    Player.stage = 20
    game_loop()


def define_branch_sean():
    Player.room = "telly"
    Player.stage = 30
    game_loop()



# Game calls
title_screen()
