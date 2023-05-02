label in_kbg:
    scene bg kbg_inside with Dissolve(0.5)
    call show_all from _call_show_all_13
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
    call reach_exit from _call_reach_exit

    if friends:
        call hide_npc from _call_hide_npc_3
    show shiro at above_right with moveinright
    "While you are heading outside you hear a few people singing a birthday song. It seems like it’s the birthday of an Asian student, Shiro."
    "After people finish the classical {i}Happy Birthday{/i} song, they continue with {i}Hanky Panky Shanghai{/i}."
    "This song is sung in the same melody as {i}Happy Birthday{/i} and often people tend to narrow their eyes with their fingers when singing it."
    "It looks like the majority enjoys singing the song."

    # Consequential choice
    call dilemma7 from _call_dilemma7

    label kingsday:
        show bg kbg_inside with Dissolve(0.5)
        if is_dutch:
            "Speaking of birthdays, you suddenly think back about this year’s {i}Kingsday{/i}."
            "Eating a {i}tompouce{/i} in the sunshine, visiting the flea market with your friends… seems like ages ago."
        else:
            "Speaking of birthdays, you suddenly remember something about a celebration called {i}Kingsday{/i}."
            "And the colour orange. Loooots of orange. Why are Dutch people so obsessed with it?"

        if friends:
            show bg kbg_inside_blurred with Dissolve(0.5)
            call show_npc from _call_show_npc_8
            s "\“Hey, can I ask you a question?\”"
            j "\“Of course!\”"
            s "\“Why do Dutch people have a thing for orange stuff? And especially during some kind of celebration day? I don’t get it.\”"
            j "\[laughs\] \“Oh, that’s because on the 27th of April, we celebrate the King’s birthday. And the word ‘orange’ is actually part of the surname from the royal bloodline, so that’s why everything is orange.\”"
            s "\“Ah, makes sense.\”"
            j "\“In Utrecht, they take {i}Kingsday{/i} very seriously. I mean, the celebrations already start at 6 PM the evening before the 27th and take exactly 24 hours.\”"
            j "\“I recommend visiting the flea market, people sell so much stuff and sometimes you find hidden gems. Oh, and eating a {i}tompouce{/i}, of course!\”"
            s "\“Sounds good, thanks for the tips!\”"
            j "\“You’re welcome!\”"

    call city_centre from _call_city_centre