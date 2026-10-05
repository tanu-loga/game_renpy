# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("You", color="#c8ffc8")
define satoko = Character("Satoko", color="#b4eee1ff")
define hikaru = Character("Hikaru",color="#e3d1ff")
define fikaru = Character("\"Hikaru\"", color="#a52020")
define nonuki = Character("????", color="#ff0000")
define ta = Character("???", color="#aa0404")
define tanaka = Character("Tanaka", color="#ff9191")
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define blackflash = Fade(0.1, 0.0, 0.5, color="#000000")


# The game starts here.

label start:
    scene bedroom evening with dissolve
    you "Not yet again."
    you "It was to be a summer no different from another."
    you "I wish it would be what I want it to be."

    menu turn_eye:
        satoko "\"Your acting different lately\""
        "Turn around":
            you "My mother looks at me, almost as if glaring."
            show Satoko
            jump eot


        "Avoid eye contact":
            you "I can picture her glaring at me, her way of \"convincing\" me to tell her information she wants to know."
            jump eot

    menu eot:
        you "..."
        "Yeah, studying for my end-of-year is no biggie":
            you "\"Yeah, studying for my end-of-year is no biggie right?\""
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
            jump twoo
    menu endingone:
        you "Hmm"
        "Yeah":
            you "\"You could have chosen not to go there, not alone. Not up a dangerous damned mountain alone\""
            hikaru "\"Perhaps it was an illusion of choice...\""
            you "\"This ain't a dream, is it?\""
            hikaru "Yeah..."
            hikaru "\"I know I can never be him.. Not to you...\""
            you "\"Maybe I won't be able to accept he's gone, ever. Not while you are here.\""
            jump dontgo
        "...":
            you "\"...\""
            hikaru "\"I know I can't replace him.\""
            hikaru "\"I have his face, his body, his memories. I behave the same way he does. I can never be him to you, right?\""
            you "\"This aint a dream, is it?\""
            jump decideendingone
    menu dontgo:
        you "..."
        "Please don't go":
            "\"Please don't go back to the mountain again. I know I'm selfish, but whatever the situation, I'll bear the sin with you.\""
            jump almostdone
        "... not a replacement":
            "\"You aren't a replacement...\""
            jump almostdone

    menu decideendingone:
        you "\"Hikaru\" nods"
        "You can try to be like him..":
            you "\"You can try to be like him, atleast...\""
            hikaru "\"Why can't I never be like him?..\""
            hikaru "\"I follow everything he does\""
            hikaru "\"Why do I feel the way I do?..\""
            hikaru "\"Why are you never satisfied?\""
            you "\"No NO NO\""
            jump rip
        "You aren't a replacement...":
            you "\"You aren't a replacement.. You are yourself to me. Always...\""
            jump almostdone


    menu rip:
        you "\"No NO NO NO\""
        "Hikaru!!":
            you "\"HIKARU COME BACK!!\""
            scene white with blackflash
            return
        "I'm sorry":
            you "\"I'm sorry!!\""
            scene white with blackflash
            return
    
label twoo:
    hikaru "\"You think so?\""
    hikaru "..."
    you "\"You have his face, his body, his memories. You are him in every way. But I know better..\""
    menu almostdone:
        hikaru "..."
        "Not gonna be back.":
            you "\"Yet, he isn't going to be back. Not now, not tommorow, not again.\""
        "I can't ask you to be like him":
            you "\"I can't ask you to be like him, Hikaru\""
    hikaru "\"I guess all we can do is go on with how things are, right?\""
    you "\"I smile\""
    you "Yeah..."
    hikaru "\"I'm sorry you can't mourn your friend as much as you probably want. Perhaps one day, you can truly honour him.\""
    you "\"Maybe someday...\""
    scene bedroom night with flash
    you "I might as well see what he wanted to give me"
    menu object:
        "Show Object":
            you "\"Dear Yoshiki, this is the time around when Hikaru died last year isn't it? Ya must have been suffering alone... I am truly sorry, and I will give you some time alone. You had me worried, sure, but ya should know the past to move forward right?\""
            you "He actually said something well-meaning for once"
            you "Know the past to move forward, huh?"
            you "I grinned to myself"
            you "I wonder where he got that from"
            return


    

        






