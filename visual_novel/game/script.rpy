# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#c8ffc8")


# The game starts here.

label start:

    scene bg room with dissolve
    show eileen happy

    e "hello"
    e "welcome to my game"

    menu:
        "go outside":
            jump outside

        "stay in this room":
            jump stay

label outside:

     scene bg whitehouse with dissolve
     show eileen concerned

     e "its freezin out here vro"
     return

label stay:
 
    show eileen happy
 
    e "Much better. It's warm in here"
    return
