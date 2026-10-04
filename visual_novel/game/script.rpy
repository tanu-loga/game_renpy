# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("You", color="#c8ffc8")
define satoko = Character("Satoko", color="#ff9393ff")


# The game starts here.

label start:

    scene bg room with dissolve
    you "Not yet again."
    you "It was to be a summer no different from another."
    you "I wish it would be what I want it to be."

    menu turn_eye:
        satoko "\"Your acting different lately\""
        "Turn around":
            you "My mother looks at me, almost as if glaring."
            jump eot


        "Avoid eye contact":
            you "I can picture her glaring at me, her way of \"convincing\" me to tell her information she wants to know."
            jump eot

    menu eot:
        you "..."
        "Yeah, studying for my end-of-year is no biggie":
            you "\"Yeah, I roll my eyes, Studying for my end-of-year is no biggie right?\""
        "I'm just focusing on studying for my end-of-year":
            you "\"I'm just focusing on studying for my end-of-year\""
    menu excuse:
        satoko "Hikaru's been asking to see you everyday"
        "I'm busy":
            you "\"Tell him I'm busy\""
            satoko "\"He asked me to give this to you. I'll give you some time now, okay? Dinner is at 8.\""
            you "\"Thank you\""

        "Mmm":
            you "Mhm"
            satoko "\"You seem to be more down overall. Do what keeps you alive and well, okay? Hikaru asked me to give this to you. I'll come back later.\"" 
            you "\"ok..\""
    
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
