label lecture_room:
    scene bg cosmos_lecture with Dissolve(0.5)
    call show_all
    "Big, grey letters on the wall spell {i}Cosmos{/i}."
    "That must be the lecture room. You open the door and enter just in time. Quickly, you pick a seat."

    if friends:
        if is_dutch:
            "Sam sits next to you."
        else:
            "Jip sits next to you."
        call hide_npc

    "The professor starts talking."
    show max at above_right with moveinright
    dr "\“Welcome everybody to your very first class of {i}Introduction to AI{/i}.\”"
    dr "\“I’m dr. Max Caulfield and I hope you all enjoyed your summer break. Let’s start.\”"
    hide max with Dissolve(0.5)
    "Dr. Caulfield’s monologue continues for a while, but soon your thoughts drift away."
    "You wonder how many international students there are at UU."

    label nr_internationals:
        if friends:
            call show_npc
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
        label .how_many:
            menu:
                "How many international students are there at UU?"

                "Around 12,000":
                    $bet = "lost"
                    $renpy.fix_rollback()
                "Around 6,000":
                    $bet = "won"
                    $renpy.fix_rollback()
                "Around 2,000":
                    $bet = "lost"
                    $renpy.fix_rollback()

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
            call hide_npc

    "After 45 minutes, it’s time for a break. You hear some students talk about their plans for going out this evening."
    show chloe at above_right with moveinright
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

    "You’re excited about discovering Utrecht’s nightlife. The more reason to find a room as soon as possible."

    label dilemma5:
        "The group continues their conversation about their evening plans."
        "Some students are talking about going to café {i}BodyTalk.{/i}"
        if is_dutch:
            j "\“What is that?\”"
        else:
            s "\“What is that?\”"
        show chloe at above_right with moveinright
        chloe "\“It’s a LGBTQ+-friendly café. I went there with my girlfriend last time.\”"
        "Suddenly, another student swamps Chloe with questions: Are you gay? Since when? How did you come out? How can you be so sure? Did you ever have a crush on one of your friends?"
        "The conversation abruptly seems to have turned into an interrogation."
        "You can see that Chloe doesn’t like it and shuts down."

        # Consequential choice
        menu:
            "What do you do?"

            "Switch the topic":
                $answer5 = "switch_topic"
                $renpy.fix_rollback()
                "You try to change the topic."
                if is_dutch:
                    j "\“Sooo, nice weather we’re having, right?\”"
                else:
                    s "\“Sooo, nice weather we’re having, right?\”"
            "Say something about it.":
                $answer5 = "talk"
                $renpy.fix_rollback()
                $score += 1
                "You let the person know that they are making Chloe uncomfortable with their questions and suggest they should stop."
                "You see that the girl is visibly relieved."
            "Wait until the topic switches, but talk later in private":
                $answer5 = "wait"
                $renpy.fix_rollback()
                "You wait until the topic switches and talk to Chloe privately how she feels about it."
                chloe "\“I got myself back together and I’m OK now. Sorry you had to see my inner meltdown.\”"
                chloe "\“I just wish it wasn’t such a big deal every time I brought it up.\”"
                if is_dutch:
                    j "\“Don’t be sorry. The one that should be, is that person who started those invasive and inappropriate questions.\”"
                else:
                    s "\“Don’t be sorry. The one that should be, is that person who started those invasive and inappropriate questions.\”"
                chloe "\“You’re right.\”"

        if friends:
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

        if answer5 == "switch_topic":
            "The group looks confused at you. However, they all sense the tense atmosphere, so they’re happy to switch the topic."
        if answer5 == "talk":
            chloe "\“Thanks so much for standing up for me! I’m so done with the fact that it’s such a big deal every time I bring it up.\”"
            chloe "\“As if my whole personality is reduced to having a girlfriend instead of a boyfriend and I owe everyone an explanation.\”"
            if is_dutch:
                j "\“Yeah, no problem! Glad I could help.\”"
                chloe "\“Are you also studying Artificial Intelligence?\”"
                j "\“Yes, I started today!\”"
                chloe "\“Cool, I tried Computing Science before, but that wasn’t really my thing. I hope this study will suit me better.\”"
                j "\“Maybe it will! It’s good that you try another study. I wouldn't know what else I would want to study besides AI.\”"
                chloe "\“You really don’t?\”"
                j "\“Hmm, thinking about it, maybe Gender Studies? But I never thought about it much further, I took a lot of science courses in high school instead of the humanities.\”"
                chloe "\“Sooo… what are you doing after class?\”"
                j "\“I’m going to the city centre. What about you?\”"
                chloe "\“Nothing much. But we can stay in touch if you’d like?\”"
                chloe "\“Can I get your number? Since you helped me, I want to take you out for a drink.\”"

                # Trivial choice
                call phone_nr
                if give_nr:
                    j "\“Here it is. Maybe your girlfriend could join too? I would like to meet her.\”"
                    chloe "\“Sure!\”"
                if not give_nr:
                    j "\“Sorry, but I don’t know you that well. But thanks for offering.\”"
                    chloe "\“No problem!\”"
            else:
                s "\“Yeah, no problem! Glad I could help.\”"
                chloe "\“Are you also studying Artificial Intelligence?\”"
                s "\“Yes, I started today!\”"
                chloe "\“Cool, I tried Computing Science before, but that wasn’t really my thing. I hope this study will suit me better.\”"
                s "\“Maybe it will! It’s good that you try another study. I wouldn't know what else I would want to study besides AI.\”"
                chloe "\“You really don’t?\”"
                s "\“Hmm, thinking about it, maybe Gender Studies? But I never thought about it much further, I took a lot of science courses in high school instead of the humanities.\”"
                chloe "\“Sooo… what are you doing after class?\”"
                s "\“I’m going to the city centre. What about you?\”"
                chloe "\“Nothing much. But we can stay in touch if you’d like?\”"
                chloe "\“Can I get your number? Since you helped me, I want to take you out for a drink.\”"

                # Trivial choice
                call phone_nr
                if give_nr:
                    s "\“Here it is. Maybe your girlfriend could join too? I would like to meet her.\”"
                    chloe "\“Sure!\”"
                if not give_nr:
                    s "\“Sorry, but I don’t know you that well. But thanks for offering.\”"
                    chloe "\“No problem!\”"

    hide chloe with Dissolve(0.5)
    "Before you can continue the conversation, the break ends. Too soon, as always."
    "The professor begins with the second part of the lecture. Although you find it interesting, your brain is still in holiday mode, which makes it hard to stay focused for more than 10 minutes."
    "Only 45 more minutes left. This is roughly 4 x 10 minutes. Should be doable."
    "After Max Caulfield explains the group project, it’s time to form groups of three and you are free to form them yourselves."

    if friends:
        if is_dutch:
            "You team up with Sam. It’s nice to have at least one familiar face in your group."
        else:
            "You team up with Jip. It’s nice to have at least one familiar face in your group."

    label dilemma6:
        "Someone approaches you."
        show val at above_right with moveinright
        v "\“Hey, I’m Val. I studied at the {i}HU{/i} (Hogeschool Utrecht, which is the university of applied sciences) first.\”"
        v "\“I don’t know anyone here. Could I join your group?\”"

        # Consequential choice
        menu:
            "What is your response?"

            "Sorry, but no.":
                call dilemma6_no
            "Let me think about it.":
                $answer6 = "maybe"
                $renpy.fix_rollback()
                "You are not sure yet."
                if is_dutch:
                    j "\“Wait, let me check with this other person real quick.\”"
                else:
                    s "\“Wait, let me check with this other person real quick.\”"
                v "\“OK, please let me know later.\”"
            "Sure!":
                call dilemma6_yes

        if friends:
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

        # Consequential choice, second chance
        if answer6 == "maybe":
            if not friends:
                scene bg black with Dissolve(0.5)
                centered "A short moment later…"
                scene bg cosmos_lecture with Dissolve(0.5)
                call show_avatar
                show val at above_right with moveinright

            "Val approaches you again."
            v "\“Hey, so have you made up your mind?\”"
            menu:
                "Can I join your group?"

                "Sorry, but no.":
                    call dilemma6_no
                "Sure!":
                    call dilemma6_yes

        # Second chance to befriend NPC if player has accepted Val and not gotten angry in Dilemma #2
        if not friends and answer6 == "yes" and answer2 != "yell":
            hide val with Dissolve(0.5)
            call show_npc
            $friends = True
            "Another student approaches you."
            if is_dutch:
                s "\“Can I also join your group?\”"
                s "\“I just arrived in the Netherlands. Today is my first day on campus.\”"
                j "\“Of course!\”"
                call convo_befriend
            else:
                j "\“Can I also join your group?\”"
                j "\“Today is my first day on campus.\”"
                s "\“Of course!\”"
                call convo_befriend

    call in_kbg
