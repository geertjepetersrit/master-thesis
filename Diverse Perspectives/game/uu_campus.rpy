label uu_campus:
    scene bg usp with Dissolve(0.5)
    call show_avatar

    "Finally, you arrived at the Utrecht Science Park, or as many just call it {i}De Uithof{/i}."

    # Consequential choice
    label bike_path:
        scene bg uithof_rainbow with Dissolve(0.5)
        call show_avatar
        if by_bike:
            "You bike towards the bike shed. Just when you want to take a turn, someone crosses the street."
            call dilemma2
        else:
            "You check out in the bus, put your OV-card away and look around. As you’re about to cross the street, someone almost crashes into you."
            call dilemma2

        call show_npc
        "You look closely. It’s the same person that confronted Chad when he made that joke!"
        "The other person recognises you too."

        if answer2 == "dodge":
            $friends = False
            "You wonder if they are headed in the same direction as you."
        elif answer2 == "yell":
            $friends = False
            if is_dutch:
                s "\“It’s you again! Watch out!\”"
                j "\“Watch out for yourself!\”"
            else:
                j "\“It’s you again! Watch out!\”"
                s "\“Watch out for yourself!\”"
        else:
            $friends = True
            if is_dutch:
                j "\“I’m so sorry!” I didn’t see you, I swear!\”"
                s "\“Don’t worry about it! I guess we were both not paying attention.\”"
                j "\“Yeah… where are you going by the way?\”"
                s "\“Some kind of building called KBG. I’m not sure where it is, I just arrived in the Netherlands. Today is my first day on campus.\”"
                call convo_befriend
            else:
                s "\“I’m so sorry!” I didn’t see you, I swear!\”"
                j "\“Don’t worry about it! I guess we were both not paying attention.\”"
                s "\“Yeah… where are you going by the way?\”"
                j "\“Some kind of building called KBG. I’m not sure where it is, today is my first day on campus.”"
                call convo_befriend

            # Avatar and NPC become friends
            label dilemma3A:
                "A group of students passes you. You hear them talking about pronouns."
                call hide_npc
                show carmen at above_right with moveinright
                carm "\“These non-binary pronouns don’t work for me. I find it too much effort, he’s not here and I don’t like him anyways.\”"
                carm "\“Plus, these pronouns don’t even exist in my native language. So I’ll just stick to using {i}him{/i}.\”"
                hide carmen
                call show_npc
                if is_dutch:
                    s "\“O my god. Did you hear that?\”"
                    j "\“Yes.\”"
                else:
                    j "\“O my god. Did you hear that?\”"
                    s "\“Yes.\”"

                # Consequential choice
                menu:
                    "\“What do you think about what Carmen said?\”"

                    "I disagree.":
                        $answer3a = "disagree"
                        $renpy.fix_rollback()
                        $score += 1
                    "No opinion.":
                        $answer3a = "no_opinion"
                        $renpy.fix_rollback()
                    "I could see why they would see it that way.":
                        $answer3a = "agree"
                        $renpy.fix_rollback()

                if is_dutch:
                    s "\“Yeah, me too.\”"
                else:
                    j "\“Yeah, me too.\”"

                if answer3a == "disagree":
                    call hide_avatar
                    show carmen at above_left with moveinleft
                    if is_dutch:
                        "Before you know it, Sam meddles in the conversation."
                        s "\“You should respect somebody’s pronouns. Regardless of their presence and if you like them or not.\”"
                        s "\“If you’re unsure how to refer to them in your native language, you could ask what their pronouns are.\”"
                    else:
                        "Before you know it, Jip meddles in the conversation."
                        j "\“You should respect somebody’s pronouns. Regardless of their presence and if you like them or not.\”"
                        j "\“If you’re unsure how to refer to them in your native language, you could ask what their pronouns are.\”"
                elif answer3a == "no_opinion":
                    "You both don’t pay further attention to the conversation and wait until they pass by."
                else:
                    call hide_avatar
                    show carmen at above_left with moveinleft
                    if is_dutch:
                        "Before you know it, Sam meddles in the conversation."
                        s "\“I understand your reasoning. Otherwise you have to invent a word that doesn’t even exist in your native language.\”"
                    else:
                        "Before you know it, Jip meddles in the conversation."
                        j "\“I understand your reasoning. Otherwise you have to invent a word that doesn’t even exist in your native language.\”"

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

                scene bg uithof_rainbow with Dissolve(0.5)
                if answer3a != "no_opinion":
                    "Before you can think further about it, Carmen says:"
                    show carmen at above_left with moveinleft
                    if answer3a == "disagree":
                        carm "\“I tried asking his pronouns once, but they just don’t stick with me. I can’t get used to it and I hardly find it the effort, since I rarely see that person.\”"
                        if is_dutch:
                            call show_npc
                            s "\“OK, but I think you should give it another shot and ask again. It may not seem a big deal to you, but it can mean a lot to them.\”"
                        else:
                            call show_npc
                            j "\“OK, but I think you should give it another shot and ask again. It may not seem a big deal to you, but it can mean a lot to them.\”"
                        carm "\“Hmm, maybe you do have a point… I’ll think about it.\”"
                    else:
                        carm "\“Yep, you read my mind. Look, I'm not trying to be a bad person. In my native language, I’m just used to binary pronouns.\”"

    label go_to_kbg:
        scene bg black with Dissolve(0.5)
        centered "\[beep!\] Your phone reminds you your class starts within 15 minutes. {i}Lecture 1: Introduction to AI{/i}, it says. You don’t want to be late on your first day!"
        scene bg uithof_rainbow with Dissolve(0.5)
        call show_avatar
        "You check your schedule in the UU app and it says your class is in {i}KBG Cosmos{/i}. You have no idea where that is."
        if friends:
            call show_npc
            if is_dutch:
                "You look around and see Sam."
                j "Do you want to walk to class together?"
                s "Sure!"
            else:
                "You look around and see Jip."
                s "Do you want to walk to class together?"
                j "Sure!"
        else:
            "You look around and don’t see the other person."
            "So, you use your best friend Google Maps to find your way."

        scene bg kbg_outside with Dissolve(0.5)
        call show_avatar
        "After some walking, you arrive at the KBG building. So many windows…"
        "In the distance, you also see a sign that says {i}Botanical Gardens{/i}. You put that mentally on your Utrecht bucket list. Perks of being a student is free entrance!"

        if friends:
            call show_npc
            if is_dutch:
                j "\“Hey, have you been to the Botanical Gardens before?\”"
                s "\“Not yet, but I’d like to!\”"
                j "\“Me too! Want to go together someday?\”"
                s "\“Sounds good! Do you like plants too?\”"
                j "\“I actually like skateboarding more, but I heard there’s a butterfly garden too and I just have to see it.\”"
                j "\“The {i}Morpho menelaus{/i} is my favourite. It’s the blue butterfly.\”"
                s "\“Cool! \[points at the KBG door\] Let's go inside.\”"
            else:
                s "\“Hey, have you been to the Botanical Gardens before?\”"
                j "\“Not yet, but I’d like to!\”"
                s "\“Me too! Want to go together someday?\”"
                j "\“Sounds good! Do you like plants too?\”"
                s "\“I love plants! Back at home, I have 6 pancake plants in my room. No joke.\”"
                j "\“Cool! \[points at the KBG door\] Let's go inside.\”"

    label enter_kbg:
        scene bg kbg_inside with Dissolve(0.5)
        call show_avatar
        "You go through the door and a sign says the Cosmos lecture hall is on the first floor."
        if not friends:
            label dilemma3B:
                "In front of the stairs, someone approaches you. They seem to have some kind of paper in their hand."
                show leo at above_right with moveinright
                l "\“Hey, could I ask you something really quick?\”"
                if is_dutch:
                    j "\“Of course.\”"
                    j "{i}\“I hope they don’t want to sell me some kind of newspaper subscription. I have a hard time saying ‘No’ to those things.\”{/i}"
                else:
                    s "\“Of course.\”"
                    s "{i}I hope they don’t want to sell me some kind of newspaper subscription. I have a hard time saying ‘No’ to those things.{/i}"
                l "\“I’m Leo from the Diversity & Inclusion Committee here at Utrecht University. Next month we want to raise awareness for transgender and non-binary people, as they are often misgendered or misunderstood.\”"
                l "\“To estimate how to approach this campaign, I’m gauging the student’s feelings about this. Could I ask your opinion about this topic?\”"

                # Consequential choice
                menu:
                    "\“What do you think of it?\”"

                    "Support it.":
                        $answer3b = "support"
                        $renpy.fix_rollback()
                        $score += 1
                        if is_dutch:
                            j "\“I think it’s a good idea. I think equipping people with more knowledge about the topic will definitely help. It’ll hopefully solve a lot of misunderstandings.\”"
                        else:
                            s "\“I think it’s a good idea. I think equipping people with more knowledge about the topic will definitely help. It’ll hopefully solve a lot of misunderstandings.\”"
                    "No opinion.":
                        $answer3b = "no_opinion"
                        $renpy.fix_rollback()
                        if is_dutch:
                            j "\“To be honest, I don’t know, because it doesn’t cross my mind often.\”"
                        else:
                            s "\“To be honest, I don’t know, because it doesn’t cross my mind often.\”"
                    "Be sceptical.":
                        $answer3b = "sceptic"
                        $renpy.fix_rollback()
                        if is_dutch:
                            j "\“On the one hand I think it’s good, but on the other hand, making people aware of their marginalised positions could have negative consequences, especially if it’s not in their power to change it.\”"
                            l "\“That’s true, I haven’t looked at it that way.\”"
                            l "\“We have to approach it very carefully, the last thing we want is any backlash.\”"
                        else:
                            s "\“On the one hand I think it’s good, but on the other hand, making people aware of their marginalised positions could have negative consequences, especially if it’s not in their power to change it.\”"
                            l "\“That’s true, I haven’t looked at it that way.\”"
                            l "\“We have to approach it very carefully, the last thing we want is any backlash.\”"

                l "\“Thank you for your answer and your time!\”"
                l "\“Have a nice day!\”"
                if is_dutch:
                    j "\“You too!\”"
                else:
                    s "\“You too!\”"

    label at_spar:
        scene bg spar_uni with Dissolve(0.5)
        call show_avatar
        "After climbing the stairs, a pink crocodile catches your eye. Uhm, the what?? Oh, it’s the mascot from the Spar University! You still have time for a drink."

        # Trivial choice
        label .choose_drink:
            menu:
                "What will you take?"

                "A coffee":
                    menu:
                        "How do you like your coffee?"
                        "Just black":
                            $drink = "black_coffee"
                            $renpy.fix_rollback()
                        "With sugar and cream":
                            $drink = "starbucks"
                            $renpy.fix_rollback()
                "A tea":
                    menu:
                        "Which tea flavour do you get?"
                        "Earl grey":
                            $drink = "earl_grey"
                            $renpy.fix_rollback()
                        "Melon":
                            $drink = "melon"
                            $renpy.fix_rollback()
                            if friends:
                                call show_npc
                                if is_dutch:
                                    s "\“Wait, you seriously like melon tea?\”"
                                    j "\“Yes. You don’t?\”"
                                    s "\“No… why would I drink something that tastes like warm fruit?\”"
                                    j "\“Why not? It’s delicious, you should try it.\”"
                                    s "\“No, thanks…\”"
                                else:
                                    j "\“Wait, you seriously like melon tea?\”"
                                    s "\“Yes. You don’t?\”"
                                    j "\“No… why would I drink something that tastes like warm fruit?\”"
                                    s "\“Why not? It’s delicious, you should try it.\”"
                                    j "\“No, thanks…\”"
                "Nothing":
                    $drink = "nothing"
                    $renpy.fix_rollback()
                    if is_dutch:
                        j "{i} Way too overpriced.{/i}"
                    else:
                        s "{i} Way too overpriced.{/i}"
                    "Next time you’ll just bring your own thermos."

    label dilemma4:
        scene bg kbg_door with Dissolve(0.5)
        call show_avatar
        show matilda at above_right with moveinright
        "While you are walking in the building, you see a girl who’s in a wheelchair."
        "Matilda’s struggling to open the door, but she hasn’t asked for any help."

        # Consequential choice
        menu:
            "What will you do?"

            "Pretend you don’t see her":
                $renpy.fix_rollback()
                $score -= 1
                $answer4 = "ignore"
                "You pretend not to see Matilda’s struggle."
                "When she’s looking at you, you quickly look in another direction. This isn’t your finest moment."
            "Immediately help her":
                $renpy.fix_rollback()
                $answer4 = "help"
                "You rush towards the door to hold it open."
                "Matilda looks at you with slight confusion, but quickly says:"
                m "\“I almost got it, but thanks!\”"
            "Ask if she needs any help":
                $renpy.fix_rollback()
                $score *= 2 # Double amount of points
                $answer4 = "ask"
                if is_dutch:
                    j "\“Hey, can I help you with that?\”"
                    m "\“Actually yes! I didn’t want to ask anyone, thank my ego for that. But the door is too heavy.\”"

        if friends:
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

        if answer4 != "ignore":
            "You wonder why Matilda is in a wheelchair."
            menu:
                "Will you ask?"

                "No":
                    $renpy.fix_rollback()
                    "Matilda disappears and you continue your way towards the lecture room."
                    call lecture_room
                    return
                "Yes":
                    $renpy.fix_rollback()
                    if is_dutch:
                        j "\“Hey, I hope you don’t mind that I ask this, but how did you end up in a wheelchair?\”"
                        m "\“No, it’s fine. I’ve been in a car accident that resulted in a spinal cord injury. So my legs and feet are paralysed.\”"
                        j "\“Oh… I’m very sorry to hear that.\”"
                        m "\“Thank you, but don’t be. It wasn’t your fault, right? \[laughs\]\”"
                        m "\“It also happened so long ago… I can handle myself in this wheelchair, but I still miss the things I did before the accident.\”"
                        j "\“What were those?\”"
                        m "\“Well, I used to take long walks through the parks. Utrecht has so many beautiful parks, but the {i}Máximapark{/i} is my absolute favourite.\”"
                        m "\“I can still visit the park in my wheelchair, but it’s just not the same.\”"
                        j "\“I see… I don’t know what else to say…\”"
                        m "\“It’s OK, talking about the {i}Máximapark{/i} brings up some good memories. I’m glad you asked, usually people just see me as kinda helpless and act awkward.\”"
                        m "\“I got to go now, but it was nice talking to you. Bye bye!\”"
                        j "\“I have to go too. See you later!\”"
                    else:
                        s "\“Hey, I hope you don’t mind that I ask this, but how did you end up in a wheelchair?\”"
                        m "\“No, it’s fine. I’ve been in a car accident that resulted in a spinal cord injury. So my legs and feet are paralysed.\”"
                        s "\“Oh… I’m very sorry to hear that.\”"
                        m "\“Thank you, but don’t be. It wasn’t your fault, right? \[laughs\]\”"
                        m "\“It also happened so long ago… I can handle myself in this wheelchair, but I still miss the things I did before the accident.\”"
                        s "\“What were those?\”"
                        m "\“Well, I used to take long walks through the parks. Utrecht has so many beautiful parks, but the {i}Máximapark{/i} is my absolute favourite.\”"
                        m "\“I can still visit the park in my wheelchair, but it’s just not the same.\”"
                        s "\“I see… I don’t know what else to say…\”"
                        m "\“It’s OK, talking about the {i}Máximapark{/i} brings up some good memories. I’m glad you asked, usually people just see me as kinda helpless and act awkward.\”"
                        m "\“I got to go now, but it was nice talking to you. Bye bye!\”"
                        s "\“I have to go too. See you later!\”"

    "Matilda disappears and you continue your way towards the lecture room."

    call lecture_room