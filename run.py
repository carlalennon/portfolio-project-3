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
    """Prints the title screen and options to the player."""
    print("################")
    print("# Closing Time #")
    print("################")
    print("#     PLAY     #")
    print("#     ABOUT    #")
    title_screen_selections()


# Title screen
def title_screen_selections():
    """Allows user to select play, about or quit."""
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
    """Prints information about the game."""
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
    """Starts the game"""
    Player.room = "porch"  # sets player room
    Player.score = 0
    Player.stage = 0
    Player.gameover = False
    get_name()


def get_name():
    """Gets the players name and sets the UI."""
    question_name = "What is your name?\n"
    print(question_name)
    player_name = input("> \n")
    Player.name = player_name
    set_player_ui()
    rules()


def rules():
    """Prints the rules of the game."""
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
    """Sets the players UI to default values."""
    Player.time = 0
    Player.room = "  "


"""def game_over():
    ""Ends the game and prints the game over message.""
    if choice_dict[Player.stage] == "GAME OVER":
        Player.gameover = True
        game_over_message()
    else:
        Player.gameover = False
        game_loop()"""
        

def game_over():
    """Ends the game and prints the game over message."""
    if choice_dict[Player.stage] == "GAME OVER":
        Player.gameover = True
        print(narrative_dict[Player.stage]) 
        print("GAME OVER")
        title_screen()
    else:
        Player.gameover = False
        game_loop()


def game_loop():
    """Main game loop. Calls all functions to run the game."""
    print(f"Current stage: {Player.stage}")
    room()  # Prints room player is in
    time_increment()  # Adds 1hour to each turn
    time()  # Prints time
    narrative()  # Prints narrative values
    score_add()  # Adds score
    score()  # Prints score
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
    """Increments time by 1 hour."""
    Player.time = Player.time + 1


def time():
    """Prints the time."""
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
    elif Player.time == 8:
        print("04:00")
    elif Player.time == 9:
        print("05:00")
    else:
        print("TimeError")


"""def score_add():
    ""Adds score to player.""
    if Player.stage in choice_dict:
        Player.score += choice_dict[Player.stage]["Win"]["Score"]
    else:
        return"""
    
def score_add():
    """Adds score to player or subtracts score if player loses."""
    if Player.stage in choice_dict:
        choice = player_answer()
        win = choice_dict[Player.stage]["Win"]["Choice"]
        lose = choice_dict[Player.stage]["Lose"]["Choice"]
        if choice == win:
            Player.score += choice_dict[Player.stage]["Win"]["Score"]
            flavour_print_win()  # Print the narrative after a correct answer
        elif choice == lose:
            Player.score -= choice_dict[Player.stage]["Lose"]["Score"]
            flavour_print_lose()  # Print the narrative after an incorrect answer
    else:
        return


def score():
    """Prints the players score."""
    print("Score: " + str(Player.score))


"""def narrative():
    ""Prints the narrative to the player.""
    if Player.stage == 0:
        player_input_branch_definition()
    else:
        print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
        for value in narrative_dict[Player.stage].values():
            print(value)
        print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")"""
        
        
def narrative():
    """Prints the narrative to the player."""
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    for value in narrative_dict[Player.stage].values():
        print(value)
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")


"""def player_answer():
    ""Gets the players choice and calls the win or lose functions.""
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
"""

def player_answer():
    """Gets the players choice and calls the win or lose functions."""
    if choice_dict[Player.stage] != "GAME OVER":
        print("\n Enter your choice below:")
        while True:  # Keep asking until a valid answer is given
            choice = input("> \n").lower()
            win = choice_dict[Player.stage]["Win"]["Choice"]
            lose = choice_dict[Player.stage]["Lose"]["Choice"]
            if choice == win:
                flavour_print_win()
                return choice  # Return the choice
            elif choice == lose:
                flavour_print_lose()
                return choice  # Return the choice
            else:
                print("Please enter a valid choice")
    return

def game_over_message():
    """Prints the game over message."""
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    for value in narrative_dict[Player.stage].values():
        print(value)
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    return


def flavour_print_win():
    """Prints the win flavour text and sets the narrative."""
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    for value in choice_dict[Player.stage]["Win"]["Flavour"].values():
        print(value)
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    narrative = choice_dict[Player.stage]["Win"]["narrative"]
    Player.stage = narrative
    game_over()


def flavour_print_lose():
    """Prints the lose flavour text and sets the narrative."""
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    for value in choice_dict[Player.stage]["Lose"]["Flavour"].values():
        print(value)
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    narrative = choice_dict[Player.stage]["Lose"]["narrative"]
    Player.stage = narrative
    game_over()


def player_input_branch_definition():
    """Decides the branch the player will take."""
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
    """Sets the branch to fruit machine."""
    Player.room = "fruit machine"
    Player.stage = 1
    game_loop()


def define_branch_pool():
    """Sets the branch to pool table."""
    Player.room = "pool table"
    Player.stage = 20
    game_loop()


def define_branch_sean():
    """Sets the branch to sean."""
    Player.room = "telly"
    Player.stage = 30
    game_loop()



# Game calls
title_screen()
