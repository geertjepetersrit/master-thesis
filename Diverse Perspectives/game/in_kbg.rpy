label in_kbg:
    scene bg kbg_inside with Dissolve(0.5)
    call show_all
    "Class has ended and you want to explore the city centre."
    if is_dutch:
        "You’d also like to visit the skate ramp in the {i}Griftpark{/i}. The pictures on the internet looked really cool."
        "But you don’t have your board with you right now. Maybe later this week?"
        if friends:
            "Sam goes to the centre with you."
    else:
        "You’d also like to visit this mysterious shop called {i}BLACKFISH{/i}. The pictures on the internet looked really cool and you heard that they give away free stickers."
        "But they’re closed today. Maybe later this week?"
        if friends:
            "Jip goes to the centre with you."

    "As you walk out of the lecture room, you see that the exit of the building is on the ground floor."

    # Trivial choice
    label .reach_exit:
        menu:
            "Will you take the elevator or the stairs?"

            "Elevator":
                $renpy.fix_rollback()
                "You take it easy and wait for the elevator to arrive. It doesn’t matter that it’s just for one floor."
            "Stairs":
                $renpy.fix_rollback()
                "You swiftly descend the stairs. That was a piece of cake for a young god like you."

    if friends:
        call hide_npc
    show shiro at above_right with moveinright
    "While you are heading outside you hear a few people singing a birthday song. It seems like it’s the birthday of an Asian student, Shiro."
    "After people finish the classical {i}Happy Birthday{/i} song, they continue with {i}Hanky Panky Shanghai{/i}."
    "This song is sung in the same melody as {i}Happy Birthday{/i} and often people tend to narrow their eyes with their fingers when singing it."
    "It looks like the majority enjoys singing the song."

    label dilemma7:
        # Consequential choice
        menu:
            "What do you do?"

            "Observe what will happen further":
                $answer7 = "observe"
                $renpy.fix_rollback()
                $score -= 1
                "You stand still until the group finishes the song and walks away."
            "Ask in private if Shiro is OK":
                call dilemma7_ask
            "Walk past it":
                $answer7 = "ignore"
                $renpy.fix_rollback()
                "You find birthday songs silly anyway and walk away, while giving a quick side eye."

        if friends:
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

        "Shiro walks away."
        hide shiro with Dissolve(0.5)

    label kingsday:
        if is_dutch:
            "Speaking of birthdays, you suddenly think back about this year’s {i}Kingsday{/i}."
            "Eating a {i}tompouce{/i} in the sunshine, visiting the flea market with your friends… seems like ages ago."
        else:
            "Speaking of birthdays, you suddenly remember something about a celebration called {i}Kingsday{/i}."
            "And the colour orange. Loooots of orange. Why are Dutch people so obsessed with it?"

        if friends:
            call show_npc
            s "\“Hey, can I ask you a question?\”"
            j "\“Of course!\”"
            s "\“Why do Dutch people have a thing for orange stuff? And especially during some kind of celebration day? I don’t get it.\”"
            j "\[laughs\] \“Oh, that’s because on the 27th of April, we celebrate the King’s birthday. And the word ‘orange’ is actually part of the surname from the royal bloodline, so that’s why everything is orange.\”"
            s "\“Ah, makes sense.\”"
            j "\“In Utrecht, they take {i}Kingsday{/i} very seriously. I mean, the celebrations already start at 6 PM the evening before the 27th and take exactly 24 hours.\”"
            j "\“I recommend visiting the flea market, people sell so much stuff and sometimes you find hidden gems. Oh, and eating a {i}tompouce{/i}, of course!\”"
            s "\“Sounds good, thanks for the tips!\”"
            j "\“You’re welcome!\”"

    call city_centre