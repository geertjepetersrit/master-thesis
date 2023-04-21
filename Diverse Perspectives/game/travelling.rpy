label travelling:
    scene bg hostel_outside with Dissolve(0.5)
    call show_avatar

    "After brushing your teeth and grabbing your backpack, it’s time to go to the campus. You go through the door and leave the hostel."
    "As you close your eyes, you think about your day."

    scene bg black with Dissolve(0.5)

    centered """
    While you are glad you have a place to stay for now, you would rather find housing for a longer period of time. Preferable with more space, but less expensive. \n\nLuckily, this evening you are invited for a {i}hospiteeravond{/i}.

    You wonder how the evening will play out. \n\nBasically, you are invited to a house viewing, which is called a {i}hospi{/i}, in short. The house is looking for new roommates.

    Usually, several people are invited and you have the chance to see the house and the room. \n\nA small party can be held, but in the end, it is all about who is the best match for the house.

    Or in this case: two matches, as there are two rooms available. \n\n{i}Huize Peereboom{/i} is looking for one Dutch and one international student, to maintain the balance.

    Likewise, {i}Huize Peereboom{/i} finds it important that everyone gets along well, so they prefer Dutch and international students who are already close.

    So, it seems to be in your benefit to befriend someone from a different nationality. \n\nAlso, you could try to interact with strangers too, as both could increase your chances of getting a room. \n\nYou never know when you will run into your potential roommates…

    """

    scene bg hostel_outside with Dissolve(0.5)
    call show_avatar

    if is_dutch:
        "You already imagine how it would be if you’d live there. Will your new roommates be as excited as you about playing card games?"
        "{i}Ligretto{/i} is your favourite, but you also enjoy playing {i}Saboteur{/i}."
    else:
        "You already imagine how it would be if you’d live there. Decorating your room with cute plants from that Dutch garden store-- what was it called again?"
        "{i}The Inner Time? The Intratuin?{/i} Anyway, you’re looking forward to it. Your room at home is full with pancake plants."

    "A notification from your phone brings you back to the present. You should leave now or you’ll be late!"

    # Trivial choice
    label .transport:
        menu:
            "How will you go to campus?"

            "By bike":
                $by_bike = True
                $renpy.fix_rollback()
            "By bus":
                $by_bike = False
                $renpy.fix_rollback()


    if by_bike:
        scene bg bike with Dissolve(0.5)
        call show_avatar
        "You find your keys, unlock your bike and hop on it. Just go with the flow. There is no other city in the Netherlands that has as many cyclists as Utrecht."
        "The traffic is quite overwhelming during rush hour and your top priority is not crashing into anyone or anything. Easier said than done…"
        "While you are waiting for a red light…"
        call dilemma1
    else:
        scene bg bus_inside with Dissolve(0.5)
        call show_avatar
        "You grab your OV-card and head to the nearest bus station. The bus you take has the size of three regular buses, being 25 metres long. Woah!"
        "Luckily, you find a spot that’s free. On the bus…"
        call dilemma1

    return

    # Dilemma with Chad
    label dilemma1:
        "You hear someone joking about ethnicities by using a derogatory term."
        show chad at above_right with moveinright
        c "\“Hehe, of course those {i}tacoheads{/i} take as much free food samples as possible.\”"
        hide chad with Dissolve(0.5)
        call show_npc
        if is_dutch:
            s "What’s so funny about it? I think it’s kinda offensive."
        else:
            j "What’s so funny about it? I think it’s kinda offensive."

        call hide_npc
        show chad at above_right with moveinright
        c "Whatever. I have friends who belong to this group, so I can do that. They don’t seem to mind it."

        "You decide that this is none of your business and try to ignore the conversation, but the person who confronted Chad earlier doesn’t buy it."
        "It looks like things are going south…"

        # Trivial choice
        label .confront_chad:
            menu:
                "What will you do?"

                "Wait until it passes over.":
                    $renpy.fix_rollback()
                    "You put in your earbuds and crank up the volume to 100. Bye outside world and its drama."

                "Try to cool it down.":
                    $renpy.fix_rollback()
                    "You attempt to break it off."
                    if is_dutch:
                        j "Excuse me, but I would appreciate it if you would stop arguing. It stresses me out, please. Thank you."
                    else:
                        s "Excuse me, but I would appreciate it if you would stop arguing. It stresses me out, please. Thank you."

        hide chad with Dissolve(0.5)
        "Unfortunately, your strategy doesn’t work and the two people continue disagreeing."
        "Hence, you try to distract yourself by texting your best friend, describing the situation you’re in."
        "They reply with: \“OK, yeah that sucks. I would try not to get involved in that, but what’s your own opinion about it?\”"

        # Consequential choice
        label .text_reply:
            menu:
                "\“Do you think that joke was appropriate?\”"

                "I don’t know, not enough context.":
                    $renpy.fix_rollback()
                    if is_dutch:
                        j "\“I think I can’t be the judge of that. I don’t know these people at all.\”"
                    else:
                        s "\“I think I can’t be the judge of that. I don’t know these people at all.\”"
                "No.":
                    $renpy.fix_rollback()
                    $score += 1
                    if is_dutch:
                        j "\“Of course not. People shouldn’t make jokes about this and try to come up with lame excuses when others call them out.\”"
                    else:
                        s "\“Of course not. People shouldn’t make jokes about this and try to come up with lame excuses when others call them out.\”"

        "You look up from your phone and notice the discussion has ended. At least verbally. "

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

    call uu_campus