# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Jip", color = "#0cfaf6")
define s = Character("Sam", color = "#dc0cf7")
define c = Character("Chad", color = "#83abdf")
define carm = Character("Carmen", color = "#11ed35")
define l = Character("Leo", color = "#faf211")
define m = Character("Matilda", color = "#fa9d07")
define dr = Character("dr. Caulfield", color = "#6ba2fa")
define chloe = Character("Chloe", color = "#266fff")
define v = Character("Val", color = "#f75c7d")
define sh = Character("Shiro", color = "#ffffff")
define st = Character("Steph", color = "#18f5b3")

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
        hide female_avatar with Dissolve(0.5)
    elif gender == "male":
        hide male_avatar with Dissolve(0.5)
    else:
        hide nb_avatar with Dissolve(0.5)

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
        hide male_avatar with Dissolve(0.5)
    elif gender == "male":
        hide nb_avatar with Dissolve(0.5)
    else:
        hide female_avatar with Dissolve(0.5)

    return

label show_all:
    call show_avatar
    if friends:
        call show_npc

    return

# Conversations

label convo_befriend:
    if is_dutch:
        j "\“Me too! I still need to get familiar with Utrecht. It would be easier if I already had a room here, but that’s not the case.\”"
        s "\“Same, but hopefully I can move to Utrecht soon. Tonight, I’m invited to this {i}hospi{/i}, so I might have a chance.\”"
        j "\“Really? I’m invited to a {i}hospi{/i} too! Wait, I think it’s the same one!\”"
        s "\“Then you probably also know they prefer one international student and one Dutch student who are already close.\”"
        j "\“True. But wait, that could be us, right?\”"
        s "\“Yeah, you’re right! We can become friends to improve our chances?\”"
        j "\“Sure! Sounds like a good plan.\”"
        s "\“I’m Sam by the way. And what’s your name?\”"
        j "\“Jip.\”"
    else:
        s "\“Me too! I still need to get familiar with Utrecht. It would be easier if I already had a room here, but that’s not the case.\”"
        j "\“Same, but hopefully I can move to Utrecht soon. Tonight, I’m invited to this {i}hospi{/i}, so I might have a chance.\”"
        s "\“Really? I’m invited to a {i}hospi{/i} too! Wait, I think it’s the same one!\”"
        j "\“Then you probably also know they prefer one international student and one Dutch student who are already close.\”"
        s "\“True. But wait, that could be us, right?\”"
        j "\“Yeah, you’re right! We can become friends to improve our chances?\”"
        s "\“Sure! Sounds like a good plan.\”"
        j "\“I’m Jip by the way. And what’s your name?\”"
        s "\“Sam.\”"

    return

label dilemma6_no:
    $answer6 = "no"
    $renpy.fix_rollback()
    $score -= 1
    $send_to_file("choices.txt", "\nDilemma 6: " + answer6)
    "You refuse politely and you decide to stretch the truth a little."
    if is_dutch:
        j "\“Sorry, but our group is already full.\”"
    else:
        s "\“Sorry, but our group is already full.\”"
    v "\“OK, I understand.\”"

    return

label dilemma6_yes:
    $answer6 = "yes"
    $renpy.fix_rollback()
    $score += 1
    $send_to_file("choices.txt", "\nDilemma 6: " + answer6)
    "The more diverse backgrounds, the better. You could probably learn a thing or two."
    if is_dutch:
        j "\“Of course!\”"
    else:
        s "\“Of course!\”"
    v "\““Thank you!”\”"

    return

label dilemma7_ask:
    $answer7 = "ask"
    $renpy.fix_rollback()
    $score += 1
    $send_to_file("choices.txt", "\nDilemma 7: " + answer7)
    if is_dutch:
        j "\“Hey, are you OK?\“"
    else:
        s "\“Hey, are you OK?\“"
    sh "\“To be honest, no. Not at all.\”"
    sh "\“Thank you for asking though. I realise now that I just should tell my friends to stop because it makes me uncomfortable.\”"
    sh "\“It’s so weird that it is taken for granted that people think it’s appropriate to do it just because someone is Asian…\”"
    sh "\“But besides that, my friends are actually nice people, although just a bit oblivious.\”"

    return

label dilemma10_disagree:
    if is_dutch:
        s "\“Well, I still agree to disagree. But that’s what we're friends for.\”"
        j "\“Yep.\”"
    else:
        j "\“Well, I still agree to disagree. But that’s what we're friends for.\”"
        s "\“Yep.\”"

    return