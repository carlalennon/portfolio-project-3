

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
    print("Stage: " + str(Player.stage))


# Player information
def room():
    """
    Prints the room the player is in (Indicates branch)
    """
    player_room = choice_dict[Player.stage]["room"]
    print("\n" + player_room.upper())


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
    win = choice_dict[Player.stage]["Win"]["Choice"]
    lose = choice_dict[Player.stage]["Lose"]["Choice"]
    if choice.lower() not in [win, lose]:
        print("Please enter a valid choice 4")
    if choice.lower() == win:
        flavour_print_win()
    elif choice.lower() == lose:
        flavour_print_lose()


def flavour_print_win():
    print("flavour_print_win")
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    for value in choice_dict[Player.stage]["Win"]["Flavour"].values():
        print(value)
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    narrative = choice_dict[Player.stage]["Win"]["narrative"]
    Player.stage = narrative
    game_loop()


def flavour_print_lose():
    print("flavour_print_lose")
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    for value in choice_dict[Player.stage]["Lose"]["Flavour"].values():
        print(value)
    print("~~*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*~~")
    narrative = choice_dict[Player.stage]["Lose"]["narrative"]
    Player.stage = narrative
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
        define_branch()
    elif action.lower() == "pool table":
        Player.stage == 20
    else:
        print("Please enter a valid option 2")
        action = input("> .. ")


def define_branch():
    Player.room = "fruit machine"
    Player.stage = 1
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
                0: "Sean turns to you beaming. 'Good game player name!'",
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
    6: {
        0: "This is an empty entry as a game over condition",
        "room": "outside"
    },
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
    8: {
        0: "Game over condition",
        "room": "outside"
    },
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
    12: "Game over condition",
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
    14: "Game over condition",
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
    17: "Game over condition",
    18: "Game over condition",
    19: "Game over condition",
}


# Narrative dictionary
narrative_dict = {
        0: {
             0: "You head down to your local on a Friday night,",
             1: "there's a loud buzz of conversation and music playing.",
             2: "The air smells like wood and alcohol. ",
             3: "You could go to the fruit machine to [Gamble]",
             4: "or try your luck at the [Pool table].",
             5: "The owner [Sean] is watching a game in the corner.",
             6: "[Tomas] is waving at you from the bar, over the ",
             7: "sound of a group of women at a [Birthday party].",
        },
        1: {
            0: "In the corner, a fruit machine plays a tune",
            1: "Mairead is using the fruit machine",
            2: "She catches your eye",
            3: "'Hey, player name",
            4: "This is the big one, I can feel it",
            5: "Can you [Give] me a fiver or [Not]?'",
        },
        2: {
            0: "You head to the bar and make small talk.",
            1: "Mairead feels a spark, and leans in to ",
            2: "kiss you. Do you [Kiss Her] or [Not]? ",
        },
        3: {
            0: "With a bad feeling, you lay low in a corner.",
            1: "Mairead's curse ringing in your ears, you",
            2: "Wonder if you should head to the bathroom to",
            3: "[Hide], or tough it out and [Stay] in your seat.",
        },
        4: {
            0: "You spot Sean in the corner. His team must have",
            1: "lost, he's crying quietly into a jersey. Do you",
            2: "[Ask] him what's wrong, or distract him with a",
            3: "game of [Pool?]",
        },
        5: {
            0: "Sean steps up for a challenge. He's not a very good",
            1: "player on the best of days, but he seems to be",
            2: "having a lot of fun.",
            3: "Do you [Beat] him, or let him [Win]?",
        },
        6: {
            0: "It's finally closing time. You survived the night.",
            1: "You and Sean are the last to leave. You stroll into",
            2: "the night as new friends.",
        },
        7: {
            0: "Your pride stinging, you look around for a",
            1: "peaceful resolution. Your eyes fall on the pool",
            2: "table. Will you [Challenge] him to a game or",
            3: "[Ignore] him?",
        },
        8: {
            0: "You have been thrown out of the pub.",
            1: "Game over. Try again?",
        },
        9: {
            0: "You make a break for the facilities to hide.",
            1: "In your haste, you slip and fall into a puddle.",
            2: "You are sticky and dirty, you smell foul. Do you",
            3: "take shelter in the [Birthday Party] or do you",
            4: "go and talk to [Tomas]?",
        },
        10: {
            0: "The women are having a great time at their party, they",
            1: "hardly notice as you place your drink down between pitchers",
            2: "of gin on the table.",
            3: "Suddenly, the one wearing a sash wrinkles her nose. She",
            4: "turns to the others and asks 'What's that smell?'",
            5: "Do you [Tell] them about the puddle, or [Blame] someone",
            6: "else?",
        },
        11: {
            0: "Nestled in the gang with a drink in your hand, you feel",
            1: "as though your night may finally be looking up. A song",
            2: "starts to blare, and the girls get up to dance. Do you",
            3: "[Join] them or [Not]?",
        },
        12: {
            0: "You dance the night away with your new pals. All grievances",
            1: "From earlier in the night are forgotten.",
            2: "Before you know it, it's closing time. You walk home with",
            3: "aching feet and a smile on your face.",
        },
        13: {
            0: "Tomas give you a wide grin.",
            1: "Hello, how are you?' he asks. Before",
            2: "you can answer, he launches into a long and terrible",
            3: "story about his recent health issues, the cost of petrol,",
            4: "and how immigrants are ruining everything.",
            5: "He finishes and waits for your reply. Do you [Sympathise]",
            6: "or [Ignore] him?",
        },
        14: {
            0: "After the loud sobs of the birthday girl, no one",
            1: "else in the pub is willing to talk to you.",
            2: "You leave early, hanging your head in shame.",
        },
        15: {
            0: "Tomas rattles on about how the youth of today are",
            1: "hopeless, and how telly isn't as good as it used to",
            2: "be. How much more of this can you endure?",
            3: "Can you [Listen] to some more, or do you [Stop] him?",
        },
        16: {
            0: "With a smile on your face, you thank Tomas for the",
            1: "story. You never knew he was so funny!",
            2: "He asks what you're smiling about. Do you [Tell] him",
            3: "he's secretly funny, or do you say [Nothing]?",
        },
        17: {
            0: "Tomas continues to chatter happily and buys you some",
            1: "drink to get you to stick around.",
            2: "You happily accept, and spent the night listening to",
            3: "his stories. The night flies by, and all of a sudden",
            4: "it's closing time. You walk into the night having made",
            5: "a new friend.",
        },
        18: {
            0: "When even the chattiest person in the pub won't talk",
            1: "to you, it's time to head home.",
        },
        19: {
            0: "Alone, smelling like floor water, and all the gin",
            1: "gone, it's time to head home in shame.",
            2: "Maybe you'll have a better time another night.",
        }
        
}



# Game calls
title_screen()
