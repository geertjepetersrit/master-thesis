label alarm:
    menu:
        "It’s 8:30 AM, maybe 5 more minutes?"

        "Snooze":
            $renpy.fix_rollback()
            "You hit the snooze button… zzz …"
            "But 5 minutes later, the ungodly sound wakes you again."
        "Get up":
            $renpy.fix_rollback()

    return

label gender:
    menu:
        "You look around in your hostel room and ask yourself: \“Who do I want to be?\” "

        "Female":
            $gender = "female"
            $renpy.fix_rollback()
            $send_to_file("choices.txt", "\nFemale")
        "Male":
            $gender = "male"
            $renpy.fix_rollback()
            $send_to_file("choices.txt", "\nMale")
        "Non-binary":
            $gender = "nb"
            $renpy.fix_rollback()
            $send_to_file("choices.txt", "\nNon-binary")

    return

label country:
    menu:
        "A question pops up in your head: \“What country am I from?\” "

        "the Netherlands":
            $is_dutch = True
            $renpy.fix_rollback()
            $send_to_file("choices.txt", "\nDutch")
        "Abroad":
            $is_dutch = False
            $renpy.fix_rollback()
            $send_to_file("choices.txt", "\nAbroad")

    return

label breakfast:
    menu:
        "As you get dressed and prepare for the day, you think: \“What should I eat for breakfast?\”"

        "Bread with {i}hagelslag{/i} (chocolate sprinkles)":
            $breakfast = "hagelslag"
            $renpy.fix_rollback()
            "Maybe you’ll even add a dot of peanut butter for the sweet tooth. You actually never tried it before, but you’ve heard it’s yummy."
        "Yoghurt with fruit and muesli":
            $breakfast = "yoghurt"
            $renpy.fix_rollback()
            "You slice an apple and a banana and put it in a bowl. Then you add the muesli on top. {i}Smakelijk!{\i}"
        "Nothing":
            $breakfast = "nothing"
            $renpy.fix_rollback()
            "Skipping breakfast saves time! But you put a snack in your bag to eat later. Lion candy bars are your favourite."

    return

label transport:
    menu:
        "How will you go to campus?"

        "By bike":
            $by_bike = True
            $renpy.fix_rollback()
        "By bus":
            $by_bike = False
            $renpy.fix_rollback()

    return

label choose_drink:
    menu:
        "What will you take?"

        "A coffee":
            menu:
                "How do you like your coffee?"
                "Just black":
                    $drink = "black_coffee"
                    $renpy.fix_rollback()
                    "You enjoy your black coffee."
                "With sugar and cream":
                    $drink = "starbucks"
                    $renpy.fix_rollback()
                    "You enjoy your coffee with sugar and cream."
        "A tea":
            menu:
                "Which tea flavour do you get?"
                "Earl grey":
                    $drink = "earl_grey"
                    $renpy.fix_rollback()
                    "You enjoy your earl grey tea."
                "Melon":
                    $drink = "melon"
                    $renpy.fix_rollback()
                    "You enjoy your melon tea."
                    if friends:
                        show bg spar_uni_blurred with Dissolve(0.5)
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
            show bg spar_uni_blurred with Dissolve(0.5)
            if is_dutch:
                j "{i} Way too overpriced.{/i}"
            else:
                s "{i} Way too overpriced.{/i}"
            "Next time you’ll just bring your own thermos."

    return

label how_many:
    menu:
        "How many international students are there at UU?"

        "Around 12,000":
            if friends:
                $bet = "lost"
            $renpy.fix_rollback()
        "Around 6,000":
            if friends:
                $bet = "won"
            $renpy.fix_rollback()
        "Around 2,000":
            if friends:
                $bet = "lost"
            $renpy.fix_rollback()

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

label reach_exit:
    menu:
        "Will you take the elevator or the stairs?"

        "Elevator":
            $renpy.fix_rollback()
            "You take it easy and wait for the elevator to arrive. It doesn’t matter that it’s just for one floor."
        "Stairs":
            $renpy.fix_rollback()
            "You swiftly descend the stairs. That was a piece of cake for a young god like you."

    return

label dom_height:
    # Trivial choice
    menu:
        "How tall is the Dom Tower?"

        "56 metres":
            $height = "wrong"
            $renpy.fix_rollback()
            "A quick Google search reveals that it’s actually 112 metres. Oops."
        "112 metres":
            $height = "correct"
            $renpy.fix_rollback()
            call bonus_dilemma from _call_bonus_dilemma
        "224 metres":
            $height = "wrong"
            $renpy.fix_rollback()
            "A quick Google search reveals that it’s actually 112 metres. Oops."

    return

label drink_order:
    menu:
        "What would you like to drink?"

        "A beer":
            $order = "beer"
            $renpy.fix_rollback()
        "A wine":
            $order = "wine"
            $renpy.fix_rollback()
        "A soda":
            $order = "soda"
            $renpy.fix_rollback()

    return

label colour:
    "\“Cheers!\“ you say and you both toast the glasses. As you are both enjoying your drinks, you’re chatting about all kinds of stuff."
    show bg terrace_neude_blurred with Dissolve(0.5)
    if is_dutch:
        "Sam asks:"
    else:
        "Jip asks:"
    menu:
        "\“What’s your favourite colour?\“"

        "Blue":
            $colour = "blue"
            $renpy.fix_rollback()
        "Red":
            $colour = "red"
            $renpy.fix_rollback()
        "Green":
            $colour = "green"
            $renpy.fix_rollback()

    if is_dutch:
        j "\“It’s [colour].\”"
        s "\“I thought it would be orange… Hahaha, no I’m kidding! Mine’s cerulean.\”"
        j "\“Uhm, isn’t that some kind of fancy word for ‘blue’?\”"
        s "\“Ouch, no. It’s just not the same.\”"
        j "\“Are you serious? It has the same colour as blue curaçao. And they don’t call it ‘cerulean curaçao’ either.\”"
        s "\“Fair. And that does have a nice ring to it.\”"
        j "\[laughs\] \“Hey, don’t steal my idea!\”"
        s "\“I would never…\” \[laughs\]"
    else:
        s "\“It’s [colour].\”"
        j "\“I thought it would be orange… Hahaha, no I’m kidding! Mine’s cerulean.\”"
        s "\“Uhm, isn’t that some kind of fancy word for ‘blue’?\”"
        j "\“Ouch, no. It’s just not the same.\”"
        s "\“Are you serious? It has the same colour as blue curaçao. And they don’t call it ‘cerulean curaçao’ either.\”"
        j "\“Fair. And that does have a nice ring to it.\”"
        s "\[laughs\] \“Hey, don’t steal my idea!\”"
        j "\“I would never…\” \[laughs\]"

    return

label dinner_choice:
    menu:
        "But what will you eat?"

        "Pasta pesto":
            $dinner = "pasta pesto"
            $renpy.fix_rollback()
        "A {i}Knorr Wereldgerecht{/i} (random dish)":
            $dinner = "Knorr Wereldgerecht"
            $renpy.fix_rollback()
        "{i}Stamppot{/i} (mashed potatoes and veggies, with gravy)":
            $dinner = "stamppot"
            $renpy.fix_rollback()

    return