label lecture_room:
    scene bg cosmos_lecture with Dissolve(0.5)
    call show_all from _call_show_all_14
    "Big, grey letters on the wall spell {i}Cosmos{/i}."
    "That must be the lecture room. You open the door and enter just in time. Quickly, you pick a seat."

    if friends:
        if is_dutch:
            "Sam sits next to you."
        else:
            "Jip sits next to you."
        call hide_npc from _call_hide_npc_4

    "The professor starts talking."
    show max at above_right with moveinright
    show bg cosmos_lecture_blurred with Dissolve(0.5)
    dr "\“Welcome everybody to your very first class of {i}Introduction to AI{/i}.\”"
    dr "\“I’m dr. Max Caulfield and I hope you all enjoyed your summer break. Let’s start.\”"
    hide max with Dissolve(0.5)
    show bg cosmos_lecture with Dissolve(0.5)
    "Dr. Caulfield’s monologue continues for a while, but soon your thoughts drift away."
    "You wonder how many international students there are at UU."

    label nr_internationals:
        $set_bet = False
        if friends:
            call show_npc from _call_show_npc_9
            show bg cosmos_lecture_blurred with Dissolve(0.5)
            $set_bet = True
            if is_dutch:
                s "\“I read that there are more than 35,000 students in total, so I bet around 8,000 of them are international.\”"
                s "\“Wait, let's make it a real bet. If your guess is the closest…\”"
                if drink == "melon":
                    s "\“I’ll try a cup of that ‘tasty’ melon tea you had earlier.\”"
                else:
                   s "\“I’ll buy you a drink.\”"
                s "\“But if I win, you owe me a drink.\”"
                j "\“Deal.\”"
            else:
                j "\“I read that there are more than 35,000 students in total, so I bet around 8,000 of them are international.\”"
                j "\“Wait, let's make it a real bet. If your guess is the closest…\”"
                if drink == "melon":
                    j "\“I’ll try a cup of that ‘tasty’ melon tea you had earlier.\”"
                else:
                   j "\“I’ll buy you a drink.\”"
                j "\“But if I win, you owe me a drink.\”"
                s "\“Deal.\”"

        # Trivial choice
        call how_many from _call_how_many

        "After consulting your best friend Google, you see that there are almost 6,000 international students."
        if is_dutch:
            j "{i}\“That’s interesting.\”{/i}"
        else:
            s "{i}\“That’s interesting.\”{/i}"

        if friends:
            if bet == "won":
                if drink == "melon":
                    if is_dutch:
                        j "\“Ha! Do you want that tea now or…?\”"
                        s "\“I would actually prefer never.\”"
                    else:
                        s "\“Ha! Do you want that tea now or…?\”"
                        j "\“I would actually prefer never.\”"
                else:
                    if is_dutch:
                        j "\“I guess you owe me a drink now.\”"
                        s "\“Yep, a bet is a bet!\”"
                    else:
                        s "\“I guess you owe me a drink now.\”"
                        j "\“Yep, a bet is a bet!\”"
            else:
                if is_dutch:
                    j "\“I guess I owe you a drink now.\”"
                    s "\“Yep, a bet is a bet!\”"
                else:
                    s "\“I guess I owe you a drink now.\”"
                    j "\“Yep, a bet is a bet!\”"
            call hide_npc from _call_hide_npc_5

    show bg cosmos_lecture with Dissolve(0.5)
    "After 45 minutes, it’s time for a break. You hear some students talk about their plans for going out this evening."
    call show_avatar from _call_show_avatar_7
    show chloe at above_right with moveinright
    show bg cosmos_lecture_blurred with Dissolve(0.5)
    chloe "\“Should I go to {i}Ekko{/i} or {i}Tivo{/i}?\”"
    if is_dutch:
        j "\“What’s {i}Tivo{/i}?\”"
    else:
        s "\“What’s {i}Tivo{/i}?\”"
    chloe "\“{i}Tivo{/i} is short for {i}TivoliVredenburg{/i}.\”"
    chloe "\“It’s a big building with multiple concert halls where you can listen to all kinds of music or go to a party.\”"
    chloe "\“It’s in the middle of the city centre and tonight there is a silent disco. Tickets are €9.\”"
    if is_dutch:
        j "\“Cool, thanks!\”"
    else:
        s "\“Cool, thanks!\”"
    hide chloe with Dissolve(0.5)
    show bg cosmos_lecture with Dissolve(0.5)
    "You’re excited about discovering Utrecht’s nightlife. The more reason to find a room as soon as possible."

    # Consequential choice
    call dilemma5 from _call_dilemma5

    "Before you can continue the conversation, the break ends. Too soon, as always."
    "The professor begins with the second part of the lecture. Although you find it interesting, your brain is still in holiday mode, which makes it hard to stay focused for more than 10 minutes."
    "Only 45 more minutes left. This is roughly 4 x 10 minutes. Should be doable."
    "After Max Caulfield explains the group project, it’s time to form groups of three and you are free to form them yourselves."

    if friends:
        call show_npc from _call_show_npc_10
        if is_dutch:
            "You team up with Sam. It’s nice to have at least one familiar face in your group."
        else:
            "You team up with Jip. It’s nice to have at least one familiar face in your group."

    # Consequential choice
    call hide_npc from _call_hide_npc_6
    call dilemma6 from _call_dilemma6

    call in_kbg from _call_in_kbg
