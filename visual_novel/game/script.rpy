# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("You", color="#c8ffc8")
define satoko = Character("Satoko", color="#b4eee1ff")
define hikaru = Character("Hikaru",color="#e3d1ff")
define fikaru = Character("\"Hikaru\"", color="#a52020")
define nonuki = Character("????", color="#ff0000")
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

# The game starts here.

label start:

    scene bedroom night with dissolve
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
    you "The air might as well been lead. Every conversation sounds stiff. Every movement delibrate. When did things turn out like this?"
    you "Hikaru is dead." with vpunch
    you "He has been dead for a year."
    you "\"You can come out now\""
    scene bedroom morning with flash
    you "\"Hikaru...\""
    hikaru "..."
    you "\"Why did you leave me?\""
    you "\"You had a choice\""
    you "\"You could have been alive\"" with hpunch
    you "\"You could have been with me\""
    you "\"Every single day I glance at your desk, wait for you to grab my shoulder and greet me, to laugh with and read with you, to talk with and simply just exist with you.\""
    you "\"I wish I can follow my normal life with you one more day...\""
    menu mainqendingone:
        hikaru "..."
        "Why did you die?":
            you "\"Why did you die?\""
            hikaru "\"Do you think I had a choice?\""
            jump endingone
        "You aren't real...":
            you "You aren't real, are you?"
    menu endingone:
        you "Hmm"
        "Yeah":
            you "You could have chosen not to go there, not alone. Not up a dangerous damned mountain alone"
        "...":
            you "\"...\""
            fikaru "\"I know I can't replace him.\""
            fikaru "\"I have his face, his body, his memories. I behave the same way he does. I can never be him to you, right?\""
            you "This aint a dream, is it?"
            jump decideendingone
            
    menu decideendingone:
        you "He nods"
        "You can try to be..":
            you "You can try to be like him, atleast..."


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
