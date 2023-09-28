# Player setup to hold status effects and name
class Player:
    def __init__(self):
        self.name = ''
        self.status = []
        self.room = ["porch"]


you = Player()


# Title screen 
def title_screen_selections():
    option = input(">")
    if option.lower() == "start":
        start_game()
    elif option.lower() == "character":
        character_index()
    while option.lower() not in ["start", "character", "quit"]:
        print("please enter a valid option")
        option = input(">")
        if option.lower() == "start":
            start_game()
        elif option.lower() == "character":
            character_index()
        elif option.lower() == "quit":
            sys.exit()


def title_screen():
    os.system("clear")
    print("################")
    print("# Closing Time #")
    print("################")
    print("#     PLAY     #")
    title_screen_selections()


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
    print("\n" + you.room.capitalize())
