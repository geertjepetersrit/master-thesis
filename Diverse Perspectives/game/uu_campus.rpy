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
                s "\“I’m so sorry!” I didn’t see you, I swear!\”"
                j "\“Don’t worry about it! I guess we were both not paying attention.\”"
                s "\“Yeah… where are you going by the way?\”"
                j "\“Some kind of building called KBG. I’m not sure where it is. Today is my first day on campus.\”"
                s "\“Me too! I still need to get familiar with Utrecht. It would be easier if I already had a room here, but that’s not the case.\”"
                j "\“Same, but hopefully I can move to Utrecht soon. Tonight, I’m invited to this {i}hospi{/i}, so I might have a chance.\”"
                s "\“Really? I’m invited to a {i}hospi{/i} too! Wait, I think it’s the same one!\”"
                j "\“Then you probably also know they prefer one international student and one Dutch student who are already close.\”"
                s "\“True. But wait, that could be us, right?\”"
                j "\“Yeah, you’re right! We can become friends to improve our chances?\”"
                s "\“Sure! Sounds like a good plan.\”"
                j "\“I’m Jip by the way. And what’s your name?\”"
                s "\“Sam.\”"

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
                    "\“What do you think about it?\”"

                    "I disagree.":
                        $answer3 = "disagree"
                        $renpy.fix_rollback()
                        $score += 1
                    "No opinion.":
                        $answer3 = "no_opinion"
                        $renpy.fix_rollback()
                    "I could see why they would see it that way.":
                        $answer3 = "agree"
                        $renpy.fix_rollback()

                if is_dutch:
                    s "\“Yeah, me too.\”"
                else:
                    j "\“Yeah, me too.\”"

                if answer3 == "disagree":
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
                elif answer3 == "no_opinion":
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

                if answer3 == "disagree":
                    carm "{i}\“I wasn’t talking to you, why are you interfering?!\”{/i}"
                elif answer3 == "no_opinion":
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
                if answer3 != "no_opinion":
                    "Before you can think further about it, Carmen says:"
                    show carmen at above_left with moveinleft
                    if answer3 == "disagree":
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
                j "\“The Morpho menelaus is my favourite. It’s the blue butterfly.\”"
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
                # enter leo


