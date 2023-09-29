import os

# Player setup to hold status effects and name
class Player:
    def __init__(self):
        self.name = ''
        self.status = []
        self.room = ["porch"]


you = Player()


def title_screen():
    os.system("clear")
    print("################")
    print("# Closing Time #")
    print("################")
    print("#     PLAY     #")
    print("#     ABOUT    #")
    title_screen_selections()
    

# Title screen 
def title_screen_selections():
    option = input(">")
    if option.lower() == "play":
        start_game()
    elif option.lower() == "about":
        about_game()
    while option.lower() not in ["play", "character", "quit"]:
        print("please enter a valid option")
        option = input(">")
        if option.lower() == "play":
            start_game()
        elif option.lower() == "character":
            character_index()


def about_game():
    os.system("clear")
    print("Some info about the game")
    print("Type back to exit to menu")
    back = input("> ")
    if back.lower() == "back":
        title_screen()
    else:
        print("Type back to exit to menu")
        back = input("> ")


def character_index():
    print("Placeholder charachter bio")
    print("Placeholder charachter bio")
    print("Placeholder charachter bio")
    print("Placeholder charachter bio")


# Logic
def start_game():
    return


NARRATIVE = "narrative"


player_state = {"meanie": False,
                "stinky": False,
                "cursed": False
                }


# Story/Narrative
def room():
    """
    Prints the room the player is in (Indicates branch)
    """
    print("\n" + you.room.upper())


def prompt():
    print("*~~;.....;~~*")
    print("Enter your choice below")
    action = input(">")
    valid_actions = ["pla", "negative action", "characters"]
    while action.lower() not in valid_actions:
        print("Please enter a valid action. \n")
        action = input(">")
    if action.lower() in ["positive action"]:
        advance_positive(action.lower())
    elif action.lower() in ["negative action"]:
        advance_negative(action.lower())
    elif action.lower() in ["characters"]:
        character_index()


# Player branch nested dictionaries

branch_fruit_machine = {
    1: {
        "Choice": "Give the money",
        "Win": True,
        "Flavour": {
            0: "You hand Mairead a fiver",
            1: "The machine beeps and pays out",
            2: "Mairead is delighted, and buys you a drink"
        },
        "Score": 250
    },
    2: {
        "Choice": "Do not",
        "Win": False,
        "Flavour": {
            0: "Mairead scowls at you",
            1: "She scowls darkly and spits a curse at you",
            2: "You feel a sense of dread creep over you"
        },
        "Score": -250,
        "Modifier": "Cursed for 2 turns, score will not change"
    },
    3: {
        "Choice": "Kiss her",
        "Win": False,
        "Flavour": {
            0: "You lean in to accept the kiss",
            1: "A dark shadow covers you",
            2: "Mairead's son pulls you from behind and threatens you",
            3: "How embarassing"
        },
        "Score": -100
    },
    4: {
        "Choice": "Don't kiss her",
        "Win": True,
        "Flavour": {
            0: "You freeze awkwardly",
            1: "Luckily, someone sits down at the fruit machine",
            2: "Mairead hurries over to preserve her winning streak"
        },
        "Score": 100
    },
    5: {
        "Choice": "Challenge him",
        "Win": True,
        "Flavour": {
            0: "Mairead's son is drunk",
            1: "The game is an easy win for you",
            2: "You shake hands and part ways as equals"
        },
        "Score": 250
    },
    6: {
        "Choice": "Don't challenge him",
        "Win": False,
        "Flavour": {
            0: "He calls you a wimp",
            1: "He assures you he will meet you outside later",
            2: "You'd better not leave early tonight..."
        },
        "Score": -250,
        "Modifier": "Enemy: You will be beaten if leaving before closing time"
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




def player_choice(action):
    """
    Abtracts player input
    """
    ask = ("What will you do?")
    ans = input(ask)


def game_loop():
    room()
    time()
    story()
    prompt()


# taken from video tutorial baober
def start_game():
    # clear terminal here
    question_name = "What is your name?\n"
    player_name = input("> ")
    Player.name = player_name
    return player_name


### Introduction
introduction1 = "Welcome, " ## add player name here
intruduction2 = "the pub is open and I am describing it now" + "\n"


# Game calls 
title_screen()