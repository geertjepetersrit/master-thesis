label uu_campus:
    scene bg usp with Dissolve(0.5)
    call show_avatar from _call_show_avatar_19

    "Finally, you arrived at the Utrecht Science Park, or as many just call it {i}De Uithof{/i}."

    # Consequential choice
    label bike_path:
        scene bg uithof_rainbow with Dissolve(0.5)
        call show_avatar from _call_show_avatar_20
        if by_bike:
            "You bike towards the bike shed. Just when you want to take a turn, someone crosses the street."
            call dilemma2 from _call_dilemma2
        else:
            "You check out in the bus, put your OV-card away and look around. As you’re about to cross the street, someone almost crashes into you."
            call dilemma2 from _call_dilemma2_1

        call show_npc from _call_show_npc_11
        "You look closely. It’s the same person that confronted Chad when he made that joke!"
        "The other person recognises you too."

        if answer2 == "dodge":
            $friends = False
            "You wonder if they are headed in the same direction as you."
        elif answer2 == "yell":
            show bg uithof_rainbow_blurred with Dissolve(0.5)
            $friends = False
            if is_dutch:
                s "\“It’s you again! Watch out!\”"
                j "\“Watch out for yourself!\”"
            else:
                j "\“It’s you again! Watch out!\”"
                s "\“Watch out for yourself!\”"
        else:
            show bg uithof_rainbow_blurred with Dissolve(0.5)
            $friends = True
            if is_dutch:
                j "\“I’m so sorry!” I didn’t see you, I swear!\”"
                s "\“Don’t worry about it! I guess we were both not paying attention.\”"
                j "\“Yeah… where are you going by the way?\”"
                s "\“Some kind of building called KBG. I’m not sure where it is, I just arrived in the Netherlands. Today is my first day on campus.\”"
                call convo_befriend from _call_convo_befriend_2
            else:
                s "\“I’m so sorry!” I didn’t see you, I swear!\”"
                j "\“Don’t worry about it! I guess we were both not paying attention.\”"
                s "\“Yeah… where are you going by the way?\”"
                j "\“Some kind of building called KBG. I’m not sure where it is, today is my first day on campus.”"
                call convo_befriend from _call_convo_befriend_3

            # Avatar and NPC become friends
            call dilemma3A from _call_dilemma3A

    label go_to_kbg:
        scene bg black with Dissolve(0.5)
        centered "\[beep!\] Your phone reminds you your class starts within 15 minutes. \n\n{i}Lecture 1: Introduction to AI{/i}, it says. You don’t want to be late on your first day!"
        scene bg uithof_rainbow with Dissolve(0.5)
        call show_all from _call_show_all_17
        "You check your schedule in the UU app and it says your class is in {i}KBG Cosmos{/i}. You have no idea where that is."
        if friends:
            show bg uithof_rainbow_blurred with Dissolve(0.5)
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
        call show_all from _call_show_all_18
        "After some walking, you arrive at the KBG building. So many windows…"
        "In the distance, you also see a sign that says {i}Botanical Gardens{/i}. You put that mentally on your Utrecht bucket list. Perks of being a student is free entrance!"

        if friends:
            show bg kbg_outside_blurred with Dissolve(0.5)
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
        scene bg kbg_entrance with Dissolve(0.5)
        call show_all from _call_show_all_19
        "You enter the KBG building, trying not to get hit by the rotating door."
        "It’s harder than it looks."
        scene bg kbg_inside with Dissolve(0.5)
        call show_all from _call_show_all_20
        "As you made it through, you see a sign that says the Cosmos lecture hall is on the first floor."
        if not friends:
            call dilemma3B from _call_dilemma3B

    label at_spar:
        scene bg spar_uni with Dissolve(0.5)
        call show_all from _call_show_all_21
        "After climbing the stairs, a pink crocodile catches your eye. Uhm, the what?? Oh, it’s the mascot from the Spar University! You still have time for a drink."

        # Trivial choice
        call choose_drink from _call_choose_drink

    call dilemma4 from _call_dilemma4

    call lecture_room from _call_lecture_room