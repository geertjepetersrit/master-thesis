# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Jip", color = "#0cfaf6")
define s = Character("Sam", color = "#dc0cf7")
define c = Character("Chad", color = "#83abdf")
define carm = Character("Carmen", color = "#11ed35")

# Define positions of the characters
transform above_left:
    xanchor 0.0
    yanchor 1.0
    ypos 810
    xpos 100

transform above_right:
    xanchor 1.0
    yanchor 1.0
    ypos 810
    xpos 1820

# Show and hide characters
label show_avatar:
    if gender == "female":
        show female_avatar at above_left with moveinleft
    elif gender == "male":
        show male_avatar at above_left with moveinleft
    else:
        show nb_avatar at above_left with moveinleft

    return

label hide_avatar:
    if gender == "female":
        hide female_avatar
    elif gender == "male":
        hide male_avatar
    else:
        hide nb_avatar

    return

label show_npc:
    if gender == "female":
        show male_avatar at above_right with moveinright
    elif gender == "male":
        show nb_avatar at above_right with moveinright
    else:
        show female_avatar at above_right with moveinright

    return

label hide_npc:
    if gender == "female":
        hide male_avatar
    elif gender == "male":
        hide nb_avatar
    else:
        hide female_avatar

    return

# Perspective switches
label ps_chad:
    show chad at above_left with moveinleft
    c "{i}\“Oh geez, people are so sensitive these days! Who do you think you are?! You don’t know anything about me or my friends. Back off.\”{/i}"
    c "{i}\“You got nothing to say anymore? Then my logic must be solid.\”{/i}"

    return

label convo_chad:
    show chad at above_right with moveinright
    if is_dutch:
        j "That was weird…"
        c "Yeah, I noticed it too…"
        j "Do you have any idea what happened?"
        c "No clue… at all."
    else:
        s "That was weird…"
        c "Yeah, I noticed it too…"
        s "Do you have any idea what happened?"
        c "No clue… at all."

    return

# Choice options
label dilemma2:
    menu:
        "What will you do?"

        "Dodge them and pretend it didn’t happen.":
            $answer2 = "dodge"
            $renpy.fix_rollback()
        "Yell at them and get angry.":
            $answer2 = "yell"
            $renpy.fix_rollback()
            $score -= 1
        "Stop and ask them where they are going.":
            $answer2 = "stop"
            $renpy.fix_rollback()
            $score += 1

    return