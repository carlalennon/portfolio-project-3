

# Player setup to hold status effects and name
class Player:
    def __init__(self):
        self.name = ''
        self.status = []
        self.room = ''
        self.score = 0
        self.stage = 0
        self.branch = ''


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
    print("title_screen_selections")
    option = input(">")
    if option.lower() == "play":
        start_game()
    elif option.lower() == "about":
        about_game()
    while option.lower() not in ["play", "about", "quit"]:
        print("please enter a valid option")
        option = input(">")
        if option.lower() == "play":
            start_game()
        elif option.lower() == "about":
            about_game()


def about_game():
    print("Some info about the game")
    print("Type back to exit to menu")
    back = input("> ")
    if back.lower() == "back":
        title_screen()
    else:
        print("Type back to exit to menu")
        back = input("> ")


# Logic
def start_game():
    Player.room = "porch"  # sets player room
    Player.score = 0
    Player.stage = 0
    Player.branch = 0
    get_name()


def get_name():
    print("get_name")
    question_name = "What is your name?\n"
    print(question_name)
    player_name = input("> ")
    Player.name = player_name
    rules()


def rules():
    print("rules")
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    print("\n Weclome, " + Player.name + ".")
    print("\n You must survive until midnight")
    print("Make good choices...\n")
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    player_input_branch_definition()


def game_loop():
    print("game_loop")
    debug_player_stage()
    room()
    time()
    score()
    narrative()
    player_answer()
    


def debug_player_stage():
    print("debug_stage")
    print("Stage: " + str(Player.stage))


# Player information
def room():
    """
    Prints the room the player is in (Indicates branch)
    """
    print("\n" + Player.room.upper())


def time():
    if Player.stage == 0:
        print("20:00")
    elif Player.stage == 1:
        print("21:00")
    elif Player.stage == 2:
        print("22:00")
    elif Player.stage == 3:
        print("23:00")
    elif Player.stage == 4:
        print("00:00")
    elif Player.stage == 5:
        print("01:00")
    else:
        print("timeError")


def score():
    print("Score: " + str(Player.score))


def narrative():
    print("narrative")
    if Player.stage == 0:
        player_input_branch_definition()
    else:
        print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
        for value in narrative_dict[Player.stage].values():
            print(value)
        print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")


def player_answer():
    print("player_answer")
    print("\n Enter your choice below:")
    choice = input("> ")
    win = debug_dict[Player.stage]["Win"]["Choice"]
    lose = debug_dict[Player.stage]["Lose"]["Choice"]
    if choice.lower() not in [win, lose]:
        print("Please enter a valid choice 4")
    if choice.lower() == win:
        flavour_print_win()
    elif choice.lower() == lose:
        flavour_print_lose()


def flavour_print_win():
    print("flavour_print_win")
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    for value in debug_dict[Player.stage]["Win"]["Flavour"].values():
        print(value)
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    Player.stage = Player.stage + 1
    game_loop()


def flavour_print_lose():
    print("flavour_print_lose")
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    for value in debug_dict[Player.stage]["Lose"]["Flavour"].values():
        print(value)
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    Player.stage = Player.stage + 1
    game_loop()


def player_input_branch_definition():
    print("player_input_branch_definition")
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    for value in narrative_dict[Player.stage].values():
        print(value)
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    print("================================")
    action = input("> ")
    valid_actions = ["gamble", "pool table", "sean", "tomas", "birthday party"]
    while action.lower() not in valid_actions:
        print("Please enter a valid action. 1\n")
        action = input("> ")
    if action.lower() == "gamble":
        branch_fruit_machine_init()
        Player.branch = 1
    else:
        print("Please enter a valid option 2")
        action = input("> .. ")


def branch_fruit_machine_init():
    print("branch_fruit_machine_init")
    Player.room = "fruit machine"
    Player.branch = 1
    Player.stage = 1
    print("Fruit machine branch initiated")
    game_loop()                                                


debug_dict = {
    1: {
        "Win": {
            "Choice": "give",
            "Flavour": {
                0: "You hand Mairead a fiver",
                1: "The machine beeps and pays out",
                2: "Mairead is delighted, and buys you a drink"
            },
            "Score": 250,
            "Branch Modifier": 10
        },
        "Lose": {
            "Choice": "not",
            "Flavour": {
                0: "Mairead scowls at you",
                1: "She scowls darkly and spits a curse at you",
                2: "You feel a sense of dread creep over you"
            },
            "Score": -250,
            "Branch Modifier": 20
        }
    },
    2: {
        "Win": {
            "Choice": "not",
            "Flavour": {
                 0: "You freeze awkwardly",
                 1: "Luckily, someone sits down at the fruit machine",
                 2: "Mairead hurries over to preserve her winning streak"
            },
            "Score": 100,
            "Branch Modifier": 30
        },
        "Lose": {
             "Choice": "kiss her",
             "Flavour": {
                0: "You lean in to accept the kiss",
                1: "A dark shadow covers you",
                2: "Mairead's son pulls you from behind and threatens you",
                3: "How embarassing"
             },
             "Score": -100,
             "Branch Modifier": 40
        }
    },
    3: {
        "Win": {
                "Choice": "Challenge him",
                "Win": True,
                "Flavour": {
                    0: "Mairead's son is drunk",
                    1: "The game is an easy win for you",
                    2: "You shake hands and part ways as equals"
                },
                "Score": 250
                },
        "Lose": {
                "Choice": "Don't challenge him",
                "Win": False,
                "Flavour": {
                    0: "He calls you a wimp",
                    1: "He assures you he will meet you outside later",
                    2: "You'd better not leave early tonight..."
                },
                "Score": -250,
                "Modifier": "Enemy: You will be beaten if leaving before closing time"
                }
        },
    4: {
        "Win": {

        },
        "Lose": {

        }
    },
    5: {
        "Win": {

        },
        "Lose": {

        }
    },
}


# Narrative dictionary
narrative_dict = {
        0: {
             0: "You enter the pub",
             1: "Description",
             2: "More description",
             3: "You could go to the fruit machine to [Gamble]",
             4: "or try your luck at the [Pool table].",
             5: "The owner [Sean] is watching a game in the corner.",
             6: "[Tomas] is waving at you from the bar, over the ",
             7: "sound of a group of women at a [Birthday party]."
        },
        1: {
            0: "In the corner, a fruit machine plays a tune",
            1: "Mairead is using the fruit machine",
            2: "She catches your eye",
            3: "'Hey, ",
            4: "This is the big one, I can feel it",
            5: "Can you [Give] me a fiver or [Not]?'"
        },
        2: {
            0: "You head to the bar and make small talk.",
            1: "Mairead feels a spark, and leans in to ",
            2: "kiss you. Do you [Kiss Her] or [Not]? "
        },
        3: {
            0: "[Challenge] him to pool",
            1: "Do [Not]"
        },
        4: {
            0: "You have won"
        }
}
# Player branch nested dictionaries
old = {
    5: {
        '''"Choice": "Challenge him",
        "Win": True,
        "Flavour": {
            0: "Mairead's son is drunk",
            1: "The game is an easy win for you",
            2: "You shake hands and part ways as equals"
        },
        "Score": 250'''
    },
    6: {
        '''"Choice": "Don't challenge him",
        "Win": False,
        "Flavour": {
            0: "He calls you a wimp",
            1: "He assures you he will meet you outside later",
            2: "You'd better not leave early tonight..."
        },
        "Score": -250,
        "Modifier": "Enemy: You will be beaten if leaving before closing time"'''
    },
    7: {
        "Choice": "Beat Sean at pool",
        "Win": False,
        "Flavour": {
            0: "Sean is annoyed at your insolence",
            1: "He throws you out of his bar",
            2: "Mairead's son beats you as he turns a blind eye"
        },
        "Score": -250,
        "Modifer": "This is a game over."
    },
    8: {
        "Choice": "Let Sean win at pool",
        "Win": True,
        "Flavour": {
            0: "Sean is glad of the distraction",
            1: "He feels like a winner!",
            2: "He gives you a drink -- on the house"
        },
        "Score": 250
    },
    9: {
        "Win": True,
        "Flavour": {
            0: "It's closing time already, your night is over",
            1: "Mairead's son is nowhere to be seen as you leave the bar",
            2: "You walk into the night with Sean as a new friend"
        }
    },
    10: {
        "Choice": "Hide in the bathroom",
        "Win": False,
        "Flavour": {
            0: "On the way to the loo, you slip in a puddle",
            1: "You're sticky and dirty now",
            2: "Your pride stinging, you head to the bar"
        },
        "Score": -100
    },
    11: {
        "Choice": "Ask Sean what's wrong",
        "Win": False,
        "Flavour": {
            0: "He obviously doesn't want to talk about it",
            1: "What's wrong with you?"
        },
        "Score": -100
    }
}


# Game calls
title_screen()
