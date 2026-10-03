# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#c8ffc8")


# The game starts here.

label start:

    scene bg room with dissolve
    show renpy

    e "You've been acting a bit more strange lately, Yoshiki"
    e "welcome to my game"

    menu emote:
        e "how are ya?"
        "Im good":
            e "yay"

        "not okayish rn":
            e "aw noo"


    menu:
        "go OUTSIDE!":
            jump outside

        "stay in this room":
            jump stay

label outside:

     scene bg whitehouse with dissolve
     show eileen concerned

     e "its freezin out here vrochaco"
     return

label stay:
 
    show eileen happy
 
    e "Much better. It's warm in here"
    return
