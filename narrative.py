# Narrative dictionary

# Allow run.py access to the narrative dictionary
def get_narrative_dict():
    narrative_dict = {
            0: {
                0: "You head down to your local on a Friday night,",
                1: "there's a loud buzz of conversation and music playing.",
                2: "The air smells like wood and alcohol. ",
                3: "You could go to the fruit machine to [Gamble]",
                4: "or try your luck at the [Pool table].",
                5: "The owner [Sean] is watching a game in the corner.",
                6: "Tomas is waving at you from the bar, over the ",
                7: "sound of a group of women at a Birthday party.",
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
            },
            20: {
                0: "You decide to start with a game of pool.",
                1: "The table has been taken over by a gang of youths.",
                2: "They look far too young to be in here...",
                3: "Will you clear the table by [Challenge]ing them",
                4: "or just quietly place a [Euro] on the table?"
            },
            21: {
                0: "This boy is not a very good player. You could",
                1: "beat him easily. Should you embarrass him and",
                2: "[Win] the game? Or should you [Lose]?"
            },
            22: {
                0: "High off the scent of victory, you look around to",
                1: "see who to talk to next. You could challenge [Sean]",
                2: "to a game of pool, or you could join the women at",
                3: "the [Birthday] table."
            },
            23: {
                0: "You greet the women around the table and ask if",
                1: "you can join them. They look at each other and ask",
                2: "'We heard crying, did you make someone cry earlier?'",
                3: "Do you [Confess] or do you [Lie]?"
            },
            24: {
                0: "The women allow you to sit with them. You notice the",
                1: "30th Birthday banner. You look around for the birthday",
                2: "girl. Do you [Wish] her happy birthday or [Not]?"
            },
            25: {
                0: "You spend the evening in the company of these wonderful",
                1: "women. Before you know it, it's closing time.",
                2: "You stroll home into the night, with the women's numbers",
                3: "in your pocket, and the promise to keep in touch with your",
                4: "new BFFs."
            },
            26: {
                0: "The women ask you to leave their table.",
                1: "Burning with embarassment from making two separate women",
                2: "cry, you decide to call it a night and head home."
            },
            27: {
                0: "The women look at you in disgust. They don't want to talk to",
                1: "you any more. You want to preserve the feeling of being a",
                2: "winner, so you decide to take your licks and head out early",
                3: "into the night."
            },
            28: {
                0: "That really hurt, and you wonder if you should [Rat] them out",
                1: "to the bar maid. On the other hand, you could go talk to",
                2: "[Tomas] who is waving at you from the bar."
            },
            29: {
            },
            30: {
                0: "You head to watch the game with Sean. He gestures for you",
                1: "to sit at his table. You want to cheer someone on, but who?",
                2: "       [Go Foxes]              [Go Stags!]               "
                },
            31: {
                0: "The Foxes are on fire this evening. Sean thinks it's a sure",
                1: "win. 'I'm going to place a bet, what do you say?'",
                2: "Will you [Place] a bet or [Not]?"
            },
            32: {
                0: "Sean's wife walks in. She looks around for him. Sean bolts",
                1: "to the back of the pub. She corners you and asks if you've",
                2: "seen him. Should you [Lie] or tell her the [Truth]?"
            },
            33: {
                0: "You follow Sean to the stock room, laughing. You decide to",
                1: "camp out in here for the time being. It's dusty, and the",
                2: "walls are lined with fine spirits.",
                3: "Should you [Get Comfortable] or [Stand Awkwardly]?"
            },
            34: {
                0: "You and Sean happily sup fine spirits by the neck in the",
                1: "stock room. The hours pass quickly, and it's finally",
                2: "closing time. You creep out of the stock room when everyone",
                3: "else is gone home, happy with your successful night."
            },
            35: {
                0: "Sean's wife marches past you and pulls him out by the ear.",
                1: "On the way out the door, he shouts that you are barred from",
                2: "his pub. You head home early, you can beg for his forgiveness",
                3: "another day."
            },
            36: {
                0: "Embarassed by your mistake, you rush to the bar to buy",
                1: "Sean a drink. You go to order, but wait... does Sean",
                2: "drink [Stout] or [Ale]?"
            },
            37: {
                0: "You bring the ale over to the birthday party. They are",
                1: "happy to accept any drink, and offer you a seat at their",
                2: "table.",
                3: "You notice the 'Happy Birthday' banner strung over",
                4: "the table. You turn to the woman wearing the sash.",
                5: "Do you wish her a happy [20th] birthday or a happy [30th]",
                6: "birthday?"
            },
            38: {
                0: "The birthday girl is flattered! You two really hit it",
                1: "off. You feel a spark. Do you lean in to [Kiss] her or",
                2: "[Not]?"
            },
            39: {
                0: "You continue to chat late into the night. All too soon,",
                1: "it's closing time. You head home with a new friend and a",
                2: "new contact in your phone book."
            },
            40: {
                0: "That's the final straw. Sean's had more than enough",
                1: "of you for one night. He takes one look at the weeping woman",
                2: "and shows you the door."
            },
            41: {
                0: "The smell of fine whiskey fills the air.",
                1: "Sean is furious -- you've broken an €800 bottle",
                2: "of whiskey!",
                3: "He throws you out of the pub, and you go home early."
            },
            42: {
                0: "You lean in for the kiss, and are met with a hard slap.",
                1: "Sean hears the commotion, and is more than sick of you at",
                2: "this point. He throws you out of his pub."
            }
        }
    return narrative_dict