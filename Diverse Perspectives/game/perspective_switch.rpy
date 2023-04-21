label switch_chad:
    # Perspective switch
    scene bg black with Dissolve(0.5)

    centered """
    Suddenly, you are feeling weird. You close your eyes, hoping the feeling will go away.

    Luckily, it vanishes as soon as it came.

    But when you open your eyes, you’re in Chad’s body! What’s happening?

    You can hear his thoughts, Chad seems to be continuing the argument in his head:
    """

    if by_bike:
        scene bg bike with Dissolve(0.5)
        call ps_chad
    else:
        scene bg bus_inside with Dissolve(0.5)
        call ps_chad

    # Switch back
    scene bg black with Dissolve(0.5)

    centered """
    The odd feeling returns. Once you open your eyes, you’re back in your own body. Life is… strange.

    Chad felt it too.
    """
    if by_bike:
        scene bg bike with Dissolve(0.5)
        call show_avatar
        call convo_chad

    else:
        scene bg bus_inside with Dissolve(0.5)
        call show_avatar
        call convo_chad

    scene bg black with Dissolve(0.5)

    centered """
    Before you think about what just happened, Chad and the other person leave and you continue your travel towards the campus.

    You try to look back on what was taking place just moments ago. \n\nDid you just swap bodies for a moment?

    No, that can’t be, as you couldn’t control Chad, you could only hear him thinking.

    Maybe you could use these new mind reading powers to your advantage… for the greater good, right?
    """

    return

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

label switch_carmen:
    # Perspective switch
    scene bg black with Dissolve(0.5)
    centered "The feeling of having a déjà vu pops up. Again, you can hear the thoughts of Carmen."
    scene bg uithof_rainbow with Dissolve(0.5)
    show carmen at above_left with moveinleft

    if answer3a == "disagree":
        carm "{i}\“I wasn’t talking to you, why are you interfering?!\”{/i}"
    elif answer3a == "no_opinion":
        carm "{i}\“Nobody objects, so what I said must make sense, right?\”{/i}"
    else:
        carm "{i}\“Exactly, that’s what I mean! Why do people find it such a big deal anyway?\”{/i}"

    # Switch back
    scene bg black with Dissolve(0.5)
    centered """
    You blink with your eyes and you’re back in your own body again.

    The telepathic thing still feels weird.
    """

    return

label switch_matilda:
    # Perspective switch
    scene bg black with Dissolve(0.5)
    centered "Another perspective switch! What is she thinking?"
    scene bg kbg_door with Dissolve(0.5)
    show matilda at above_left with moveinleft
    if answer4 == "ignore":
        m "{i}\“Why are you pretending not to see me? I can clearly see you. And now you look away. How rude.\”{/i}"
    elif answer4 == "help":
        m "{i}\“Maybe I could’ve done it myself, maybe not.\”{/i}"
        m "{i}\“It was kind that that person helped me, but I’m not as helpless as I may look.\”{/i}"
    else:
        m "{i}\“Oh, wow this actually saves me a lot of effort, how nice! I’m really glad you helped me, but asked first.\”{/i}"
        m "{i}\“Some people just automatically assume I can’t do anything, but that’s not the case.\”{/i}"

    # Switch back
    scene bg black with Dissolve(0.5)
    centered "Within the blink of an eye you’re back in your own body."
    scene bg kbg_door with Dissolve(0.5)
    call show_avatar
    show matilda at above_right with moveinright

    return

label switch_chloe:
    # Perspective switch
    scene bg black with Dissolve(0.5)
    centered "Before you notice, you can read the other’s mind again."
    scene bg cosmos_lecture with Dissolve(0.5)
    show chloe at above_left with moveinleft
    if answer5 == "switch_topic":
        chloe "{i}\“OK, I guess that awkward attempt kinda worked?\”{/i}"
        chloe "{i}\“But I still can’t shake the feeling of harassment, this way people will never realise how invasive and inappropriate their questions actually are.\”{/i}"
        chloe "{i}\“You wouldn’t ask a straight person the same questions, would you?\”{/i}"
    elif answer5 == "talk":
        chloe "{i}\“Wow, I’m really glad you put them in their place.\”{/i}"
        chloe "{i}\“People are sometimes just so nosey.\”{/i}"
        chloe "{i}\“You wouldn’t ask a straight person the same questions, would you?\”{/i}"
    else:
        chloe "{i}\“Thanks for checking in, but I wish you'd done that earlier. I mean, why didn’t anybody say anything?\”{/i}"
        chloe "{i}\“I feel so alone, this makes me really sad. I probably shouldn’t have mentioned it, but it still feels unfair.\”{/i}"
        chloe "{i}\“You wouldn’t ask a straight person the same questions, would you?\”{/i}"

    # Switch back
    scene bg black with Dissolve(0.5)
    centered "Nevermind…"
    scene bg cosmos_lecture with Dissolve(0.5)
    call show_avatar
    show chloe at above_right with moveinright

    return

label switch_val:
    # Perspective switch
    scene bg black with Dissolve(0.5)
    centered "Poof! Now you’re in Val’s head!"
    scene bg cosmos_lecture with Dissolve(0.5)
    show val at above_left with moveinleft
    if answer6 == "no":
        v "{i}\“Actually, I don’t understand it at all. I can’t shake the feeling that people look down on me just because I didn’t do university…\”{/i}"
    elif answer6 == "maybe":
        v "{i}\“Maybe I shouldn’t have mentioned my previous education. It seems to put me at a disadvantage.\”{/i}"
    else:
        v "{i}\“That went well. I’m glad I found a group so quickly.\”{/i}"

    # Switch back
    scene bg black with Dissolve(0.5)
    centered "Reverse poof! Now you’re back to being your old self."
    scene bg cosmos_lecture with Dissolve(0.5)
    call show_avatar
    show val at above_right with moveinright
    "Val goes back to her seat, as the lecture is almost over."
    hide val with Dissolve(0.5)

    return

label switch_shiro:
    # Perspective switch
    scene bg black with Dissolve(0.5)
    centered "Oh, there’s the switch! What are they thinking this time?"
    scene bg kbg_inside with Dissolve(0.5)
    show shiro at above_left with moveinleft
    if answer7 == "ask":
        sh "{i}\“I’m so glad that you asked. This is just the boost I needed to put an end to this nonsense.\”{/i}"
    else:
        sh "{i}\“Nobody comments on this… Maybe they don’t realise that their ‘good’ intentions come out really bad.\”{/i}"

    # Switch back
    scene bg black with Dissolve(0.5)
    centered "And now you’re back to normal."
    scene bg kbg_inside with Dissolve(0.5)
    call show_avatar
    show shiro at above_right with moveinright

    if answer7 == "ignore":
        "Now you start to feel bad for Shiro."
        "Although you don’t know him or his friends at all, maybe it’s worth a try to say something."

        # Consequential choice, second chance
        menu:
            "What will you do?"

            "Brush off the feeling and start walking faster":
                $renpy.fix_rollback()
                "Sorry, but you can’t take the whole world’s weight on your shoulders."
            "Ask if Shiro is OK":
                call dilemma7_ask

    return

#label switch_steph:
#    # Perspective switch
#    scene bg black with Dissolve(0.5)
#    centered "Oh, it’s happening again! What’s on their mind?"
#    scene bg dom_square with Dissolve(0.5)
#    show steph at above_left with moveinleft
#    if bonus_answer == "downplay":
#        st "{i}\“Why did I ask a random stranger for advice? Besides that, you probably think I’m blowing it up, but that’s not the case. I’m really struggling with it.\”{/i}"
#    else:
#        st "{i}\“They’re right, it’s my own decision to make. I guess I just needed to feel understood.\”{/i}"
#
#    # Switch back
#    scene bg black with Dissolve(0.5)
#    centered "Back to hearing only your own thoughts."
#    scene bg dom_square with Dissolve(0.5)
#    call show_avatar
#    show steph at above_right with moveinright
#
#    return