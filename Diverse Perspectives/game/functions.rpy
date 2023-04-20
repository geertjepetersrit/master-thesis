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

label show_all:
    call show_avatar
    if friends:
        call show_npc

    return

# Perspective switches
label ps_chad:
    show chad at above_left with moveinleft
    c "{i}\“Oh geez, people are so sensitive these days! Who do you think you are?! You don’t know anything about me or my friends. Back off.\”{/i}"
    c "{i}\“You got nothing to say anymore? Then my logic must be solid.\”{/i}"

    return

# Conversations
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

label phone_nr:
    menu:
        "Will you give your phone number?"

        "Yes":
            $give_nr = True
            $renpy.fix_rollback()
        "No":
            $give_nr = False
            $renpy.fix_rollback()

    return

label dilemma6_no:
    $answer6 = "no"
    $renpy.fix_rollback()
    $score -= 1
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
    if is_dutch:
        j "\“Hey, are you OK?\“"
    else:
        s "\“Hey, are you OK?\“"
    sh "\“To be honest, no. Not at all.\”"
    sh "\“Thank you for asking though. I realise now that I just should tell my friends to stop because it makes me uncomfortable.\”"
    sh "\“It’s so weird that it is taken for granted that people think it’s appropriate to do it just because someone is Asian…\”"
    sh "\“But besides that, my friends are actually nice people, although just a bit oblivious.\”"

    return

label bonus_dilemma:
    if friends:
        call hide_npc
    show steph at above_right with moveinright
    st "\“In case you’re wondering, the Dom is actually 112 metres and 32 centimetres! To get to the top, you have to take 465 steps.\”"
    st "\“People even organise stair climbing matches. I like random facts, that's why I know. People find me a bit peculiar, and they might be right.\”"
    st "\“I’m Steph, by the way.\”"
    if is_dutch:
        j "“I’m Jip. And why is that so?”"
    else:
        s "“I’m Sam. And why is that so?”"
    st "\“Just between me and you, I’m diagnosed with autism, but I don’t know if I want to tell my friends about this.\”"
    st "\“I’m afraid I will be judged differently when I do. I don’t mind telling strangers though.\”"

    # Consequential choice
    menu:
        "What would you say to Steph?"

        "Play it down":
            $bonus_answer = "downplay"
            $renpy.fix_rollback()
            if is_dutch:
                j "\“Everybody has some autistic traits and that it’s not a big deal in telling people.\”"
            else:
                s "\“Everybody has some autistic traits and that it’s not a big deal in telling people.\”"
            st "\“You’re probably right. But I’m still not sure if I’m ready for that.\”"
        "Thank and support":
            $bonus_answer = "thank_support"
            $renpy.fix_rollback()
            $score += 1
            if is_dutch:
                j "\“I can’t make that choice for you, but I support you in whatever decision you take. Thanks a lot for sharing that with me.\”"
            else:
                s "\“I can’t make that choice for you, but I support you in whatever decision you take. Thanks a lot for sharing that with me.\”"
            st "\“Thank you.\”"

    if friends:
        # Perspective switch
        scene bg black with Dissolve(0.5)
        centered "Oh, it’s happening again! What’s on their mind?"
        scene bg dom_square with Dissolve(0.5)
        show steph at above_left with moveinleft
        if bonus_answer == "downplay":
            st "{i}\“Why did I ask a random stranger for advice? Besides that, you probably think I’m blowing it up, but that’s not the case. I’m really struggling with it.\”{/i}"
        else:
            st "{i}\“They’re right, it’s my own decision to make. I guess I just needed to feel understood.\”{/i}"

        # Switch back
        scene bg black with Dissolve(0.5)
        centered "Back to hearing only your own thoughts."
        scene bg dom_square with Dissolve(0.5)
        call show_avatar
        show steph at above_right with moveinright

    "Steph smiles and walks away."
    hide steph
    call show_all

    return

label dilemma10_disagree:
    if is_dutch:
        s "\“Well, I still agree to disagree. But that’s what we're friends for.\”"
        j "\“Yep.\”"
    else:
        j "\“Well, I still agree to disagree. But that’s what we're friends for.\”"
        s "\“Yep.\”"

    return