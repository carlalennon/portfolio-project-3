# Get narrative from run.py
from narrative import get_narrative_dict

narrative_dict = get_narrative_dict()

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


choice_dict = {
    1: {
        "Win": {
            "Choice": "give",
            "Flavour": {
                0: "You hand Mairead a fiver and she put it in",
                1: "the fruit machine. The machine beeps and pays out",
                2: "a handful of change. \n",
                3: "Mairead is delighted, and buys you a drink!"
            },
            "Score": 250,
            "narrative": 2
        },
        "Lose": {
            "Choice": "not",
            "Flavour": {
                0: "Mairead scowls at you",
                1: "She scowls darkly and spits a curse at you",
                2: "You feel a sense of dread creep over you"
            },
            "Score": -250,
            "narrative": 3
        },
        "room": "fruit machine"
    },
    2: {
        "Win": {
            "Choice": "not",
            "Flavour": {
                 0: "You freeze awkwardly, unsure what to do.",
                 1: "Luckily, someone sits down at the fruit machine and",
                 2: "Mairead hurries over to preserve her winning streak."
            },
            "Score": 100,
            "narrative": 4
        },
        "Lose": {
             "Choice": "kiss her",
             "Flavour": {
                0: "You lean in to accept the kiss",
                1: "A dark shadow covers you, and a hand grabs your shoulder.",
                2: "Mairead's son pulls you from behind and threatens you",
                3: "How embarassing..."
             },
             "Score": -100,
             "narrative": 7
        },
        "room": "bar"
    },
    3: {
        "Win": {
                "Choice": "stay",
                "Win": True,
                "Flavour": {
                    0: "As you finish your drink you feel a little",
                    1: "better. With a sense of comfort, you survey",
                    2: "Your surroundings."
                },
                "Score": 250,
                "narrative": 4
                },
        "Lose": {
                "Choice": "hide",
                "Win": False,
                "Flavour": {
                    0: "As you hurry toward the facilities, you step",
                    1: "into a puddle and sprawl to the floor. You are",
                    2: "all sticky and dirty now."
                },
                "Score": -250,
                "narrative": 9
            },
        "room": "bar"
    },
    4: {
        "Win": {
            "Choice": "pool",
            "Win": True,
            "Flavour": {
                0: "Sean jumps at the distraction. He loves pool!",
                1: "'I'm the best, just don't win or I might throw",
                2: "you out of this pub! Ha ha.' "
            },
            "Score": 100,
            "narrative": 5
        },
        "Lose": {
            "Choice": "ask",
            "Win": False,
            "Flavour": {
                0: "He doesn't want to talk about it, what's",
                1: "wrong with you?",
                2: "Maybe a game of pool will cheer him up."
            },
            "Score": -100,
            "narrative": 5
        },
        "room": "bar"
    },
    5: {
        "Win": {
            "Choice": "win",
            "Win": True,
            "Flavour": {
                0: "Sean turns to you beaming. 'Good game!'",
                1: "He sources you a drink on the house."
            },
            "Score": 300,
            "narrative": 6
        },
        "Lose": {
            "Choice": "beat",
            "Win": False,
            "Flavour": {
                0: "Sean is annoyed by your insolence. He shows",
                1: "you the door."
            },
            "Score": -100,
            "narrative": 8
        },
        "room": "pool table"
    },
    6: "GAME OVER",
    7: {
        "Win": {
            "Choice": "challenge",
            "Win": True,
            "Flavour": {
                0: "Mairead's son is very drunk. It's an easy win.",
                1: "You shake hands and part ways, as equals."
            },
            "Score": 250,
            "narrative": 5
        },
        "Lose": {
            "Choice": "ignore",
            "Win": False,
            "Flavour": {
                0: "Mairead's son calls you a wimp. He assures",
                1: "you he'll see you outside later.",
                2: "You'd better not leave early tonight."
            },
            "Score": -250,
            "narrative": 5
        },
        "room": "pool table"
    },
    8: "GAME OVER",
    9: {
        "Win": {
            "Choice": "birthday party",
            "Win": True,
            "Flavour": {
                0: "You hide in the back of the group of women,",
                1: "hoping they don't notice you."
            },
            "Score": 0,
            "narrative": 10
        },
        "Lose": {
            "Choice": "tomas",
            "Win": False,
            "Flavour": {
                0: "You shuffle toward Tomas, hoping that he",
                1: "will tolerate your company."
            },
            "Score": 0,
            "narrative": 13
        },
        "room": "bar"
    },
    10: {
        "Win": {
            "Choice": "tell",
            "Win": True,
            "Flavour": {
                0: "You explain what happened to you, that you",
                1: "fell in a puddle and came here to hide so you",
                2: "wouldn't be alone.",
                3: "The group 'awwww's and hands you a gin and tonic."
            },
            "Score": 250,
            "narrative": 11
        },
        "Lose": {
            "Choice": "blame",
            "Win": False,
            "Flavour": {
                0: "You decide to blame someone. You accuse",
                1: "one of the women. She starts to cry. The other",
                2: "women are not fooled, and ask you to leave their",
                3: "table."
            },
            "Score": -300,
            "narrative": 14
        },
        "room": "birthday"
    },
    11: {
        "Win": {
            "Choice": "join",
            "Win": True,
            "Flavour": {
                0: "You get up and join them on the dance floor."
            },
            "Score": 300,
            "narrative": 12
        },
        "Lose": {
            "Choice": "not",
            "Win": False,
            "Flavour": {
                1: "You sit awkwardly among the party decorations",
                2: "as the women get up and dance."
            },
            "Score": -200,
            "narrative": 19
        },
        "room": "birthday"
    },
    12: "GAME OVER",
    13: {
        "Win": {
            "Choice": "sympathise",
            "Win": True,
            "Flavour": {
                0: "You nod your head at this rant.",
                1: "This makes Tomas very happy! He buys you a",
                2: "drink and launches into another speech..."
            },
            "Score": 100,
            "narrative": 15
        },
        "Lose": {
            "Choice": "ignore",
            "Win": False,
            "Flavour": {
                0: "You stare at Tomas, stone-faced.",
                1: "He is not happy with you.",
                2: "'I'm not making small talk with the type",
                3: "of eejit who falls into puddles!'",
                4: "He turns his back to you."
            },
            "Score": -100,
            "narrative": 18
        },
        "room": "bar"
    },
    14: "GAME OVER",
    15: {
        "Win": {
            "Choice": "listen",
            "Win": True,
            "Flavour": {
                0: "Tomas's next story is about aliens coming to",
                1: "his farm and shooting at his cows.",
                2: "It's actually pretty funny!"
            },
            "Score": 250,
            "narrative": 16
        },
        "room": "bar"
    },
    16: {
        "Win": {
            "Choice": "nothing",
            "Win": True,
            "Flavour": {
                0: "Tomas, ever the picture of manly stoicism,",
                1: "accepts your silence as a gesture of manly",
                2: "comradery."
            },
            "Score": 100,
            "narrative": 17
        },
        "Lose": {
            "Choice": "tell",
            "Win": False,
            "Flavour": {
                0: "Tomas looks hurt, he wasn't trying to be",
                1: "funny. He is no longer interested in",
                2: "talking to you."
            },
            "Score": -100,
            "narrative": 18
        },
        "room": "bar"
    },
    17: "GAME OVER",
    18: "GAME OVER",
    19: "GAME OVER",
    20: {
        "Win": {
            "Choice": "challenge",
            "Win": True,
            "Flavour": {
                0: "They are impressed by your confident",
                1: "tone. The biggest boy agrees to play",
                2: "you."
            },
            "Score": 200,
            "narrative": 21
        },
        "Lose": {
            "Choice": "euro",
            "Win": False,
            "Flavour": {
                0: "They do not respect pool table ettiquitte.",
                1: "They throw the euro at your head.",
                2: "You retreat and look around for something",
                3: "else to do."
            },
            "Score": -100,
            "narrative": 28
        },
        "room": "pool table"
    },
    21: {
        "Win": {
            "Choice": "lose",
            "Win": True,
            "Flavour": {
                0: "You decide to let this one slide and",
                1: "tank the game. The boy is delighted!",
                2: "It's winner stays on, so you're off the",
                3: "pool table for now."
            },
            "Score": 100,
            "narrative": 4
        },
        "Lose": {
            "Choice": "win",
            "Win": False,
            "Flavour": {
                0: "You easily beat the boy while all his",
                1: "friends watch. One of the girls starts to",
                2: "cry. You've ruined her fake 18th birthday."
            },
            "Score": -200,
            "narrative": 22
        },
        "room": "pool table"
    },
    22: {
        "Win": {
            "Choice": "sean",
            "Win": True,
            "Flavour": {
                0: "You approach Sean and tell him the",
                1: "table is yours. He assures you that",
                2: "won't be the case for long."
            },
            "Score": 0,
            "narrative": 5
        },
        "Lose": {
            "Choice": "birthday",
            "Win": True,
            "Flavour": {
                0: "You decide to leave the table",
                1: "on a high, and wander over to the",
                2: "lively birthday party."
            },
            "Score": 0,
            "narrative": 23
        },
        "room": "pool table"
    },
    23: {
        "Win": {
            "Choice": "lie",
            "Win": True,
            "Flavour": {
                0: "You deny the whole thing, and swear",
                1: "the girl was crying about something else."
            },
            "Score": 200,
            "narrative": 24
        },
        "Lose": {
            "Choice": "confess",
            "Win": True,
            "Flavour": {
                0: "You confess it was you who made her cry. After",
                1: "all, it's the right thing to do."
            },
            "Score": -250,
            "narrative": 27
        },
        "room": "birthday party"
    },
    24: {
            "Win": {
                "Choice": "not",
                "Win": True,
                "Flavour": {
                    0: "You stay quiet as the birthday girl returns",
                    1: "from the bar. She's happy to meet you!"
                },
                "Score": 100,
                "narrative": 25
            },
            "Lose": {
                "Choice": "wish",
                "Win": False,
                "Flavour": {
                    0: "You wish the woman closest to you a happy",
                    1: "birthday. She bursts into tears. It's not",
                    2: "her 30th birthday, it's her mother's fake",
                    3: "30th birthday!"
                },
                "Score": -100,
                "narrative": 26
            },
            "room": "birthday PARTY"
        },
    25: "GAME OVER",
    26: "GAME OVER",
    27: "GAME OVER",
    28: {
            "Win": {
                "Choice": "tomas",
                "Win": True,
                "Flavour": {
                    0: "You leave the children behind and",
                    1: "leave for the bar to chat to Tomas."
                },
                "Score": 250,
                "narrative": 13
            },
            "Lose": {
                "Choice": "rat",
                "Win": False,
                "Flavour": {
                    0: "You decide to rat them out to the",
                    1: "bar maid. She is a classmate of theirs",
                    2: "and doesn't appreciate it. She give you",
                    3: "a dirty look and short changes you."
                },
                "Score": -100,
                "narrative": 4
            },
            "room": "bar"
        },
    29: "Placeholder for extra question",
    30: {
            "Win": {
                "Choice": "go foxes",
                "Win": True,
                "Flavour": {
                    0: "Sean cheers along with you.",
                    1: "You can't be sure, but it seems the",
                    2: "Foxes are playing better than before."
                },
                "Score": 250,
                "narrative": 31
            },
            "Lose": {
                "Choice": "go stags",
                "Win": False,
                "Flavour": {
                    0: "Sean's face sours.",
                    1: "Oops, wrong team!"
                },
                "Score": -100,
                "narrative": 36
            },
            "room": "telly"
        },
    31: {
            "Win": {
                "Choice": "place",
                "Win": True,
                "Flavour": {
                    0: "The bet pays off! Sean is happy",
                    1: "and buys you a drink."
                },
                "Score": 250,
                "narrative": 32
            },
            "Lose": {
                "Choice": "not",
                "Win": False,
                "Flavour": {
                    0: "Sean is disappointed you don't",
                    1: "believe in the team.",
                    2: "You head to the bar to escape his",
                    3: "scorn, and run into Tomas."
                },
                "Score": -100,
                "narrative": 13
            },
            "room": "telly"
        },
    32: {
            "Win": {
                "Choice": "lie",
                "Win": True,
                "Flavour": {
                    0: "You say you haven't seen him.",
                    1: "She looks skeptical, but leaves you alone."
                },
                "Score": 100,
                "narrative": 33
            },
            "Lose": {
                "Choice": "truth",
                "Win": False,
                "Flavour": {
                    0: "Sean's wife is furious. He said he",
                    1: "was only stepping out for milk!"
                },
                "Score": -250,
                "narrative": 35
            },
            "room": "telly"
        },
    33: {
        "Win": {
            "Choice": "stand awkwardly",
            "Win": True,
            "Flavour": {
                0: "You are careful not to knock anything over",
                1: "as you stand poker-straight in the corner.",
                2: "Besides, there are probably spiders on the floor.",
                3: "Sean cracks open a bottle of whiskey."
            },
            "Score": 100,
            "narrative": 34
        },
        "Lose": {
            "Choice": "get comfortable",
            "Win": False,
            "Flavour": {
                0: "You slump down against a musty wall.",
                1: "In the dark, you feel something bump",
                2: "your head. Something falls from the shelf",
                3: "behind you and smashes on the floor."
            },
            "Score": -300,
            "narrative": 41
        },
        "room": "stock room"
    },
    34: "GAME OVER",
    35: "GAME OVER",
    36: {
        "Win": {
            "Choice": "stout",
            "Win": True,
            "Flavour": {
                0: "You hand Sean the stout.",
                1: "He sips it, and thanks you",
                2: "with a frothy moustache on",
                3: "his lip."
            },
            "Score": 200,
            "narrative": 32
        },
        "Lose": {
            "Choice": "ale",
            "Win": False,
            "Flavour": {
                0: "Sean wrinkles his nose at",
                1: "the ale. 'I wouldn't drink",
                2: "that!'",
                3: "Sean's having a terrible time.",
                4: "Maybe you should do something",
                5: "else."
            },
            "Score": -200,
            "narrative": 37
        },
        "room": "telly"
    },
    37: {
        "Win": {
            "Choice": "20th",
            "Win": True,
            "Flavour": {
                0: "It's actually her 30th, but",
                1: "she's really flattered!"
            },
            "Score": 300,
            "narrative": 38
        },
        "Lose": {
            "Choice": "30th",
            "Win": False,
            "Flavour": {
                0: "It's actually her 20th! She's",
                1: "really upset, and starts to sob",
                2: "loudly."
            },
            "Score": -200,
            "narrative": 40
        }
    },
    38: {
        "Win": {
            "Choice": "not",
            "Win": True,
            "Flavour": {
                0: "You continue the conversation",
                1: "without sexually harassing anyone."
            },
            "Score": 100,
            "narrative": 39
        }
    },
    39: "GAME OVER",
    40: "GAME OVER",
    41: "GAME OVER",
    42: "GAME OVER"
}



# Game calls
title_screen()
