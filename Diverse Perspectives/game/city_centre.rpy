label city_centre:
    label go_to_cc:
        if by_bike:
            scene bg minnaert_bike_shed with Dissolve(0.5)
            call show_all
            "As you leave the KBG, you look for your bike."
            if friends:
                if is_dutch:
                    "Sam is by bike too."
                else:
                    "Jip is by bike too."
            scene bg uithof_rainbow with Dissolve(0.5)
            call show_all
            "You bike towards the city centre and park your bike in one of the sheds underground."
            "The shed is guarded and the first 24 hours are free. Plus, you don’t risk that your bike will be taken away by the municipality."
        else:
            scene bg usp_bus_stop with Dissolve(0.5)
            call show_all
            "As you leave the KBG, you look for the bus stop."
            if friends:
                if is_dutch:
                    "Sam is by bus too."
                else:
                    "Jip is by bus too."
            scene bg usp_bus with Dissolve(0.5)
            call show_all
            "You take bus 28 and get off at the stop called ‘Neude’"

    label dom_tower:
        scene bg city_centre with Dissolve(0.5)
        call show_all
        "You walk along the {i}Oudegracht{/i}, which is a street in the heart of the centre. The length of the street is almost 2 km!"
        "It’s also the street where the tiniest house in Utrecht is located: at number 133. At the other side of the street is the oldest house in Utrecht: at number 114."
        "In fact, that house is named {i}Drakenborch{/i} and used to be a castle."

        "From the {i}Oudegracht{/i}, you could already see the Dom Tower. Impressive!"

        scene bg dom_square with Dissolve(0.5)
        call show_all
        "After a few minutes of walking, you find yourself at the Dom Square, looking at the Dom Tower. You are wondering how tall the Dom actually is."

        # Only possible when friends
        label .another_bet:
            if bet == "won":
                if is_dutch:
                    j "\“Wanna bet again?\”"
                    s "\“I’ll skip this one.\”"
                else:
                    s "\“Wanna bet again?\”"
                    j "\“I’ll skip this one.\”"
            if bet == "lost":
                if is_dutch:
                    s "\“Wanna bet again?\”"
                    j "\“I’ll skip this one.\”"
                else:
                    j "\“Wanna bet again?\”"
                    s "\“I’ll skip this one.\”"

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
                    call bonus_dilemma
                "224 metres":
                    $height = "wrong"
                    $renpy.fix_rollback()
                    "A quick Google search reveals that it’s actually 112 metres. Oops."

    "You’ve also read on the internet that Utrecht is the city where Miffy was born. Or in Dutch: {i}Nijntje{/i}."
    "You want to visit Miffy’s statue at the {i}Nijntje pleintje{/i} (Miffy square)."
    scene bg dom_tower with Dissolve(0.5)
    call show_all
    "As you’re walking, you cross the {i}Janskerkhof{/i}. This place has the oldest bookstore in the Netherlands, because the first Dutch book was printed in Utrecht."
    "Moreover, every Saturday, the parking space at the {i}Janskerkhof{/i} turns into a flower market."

    scene bg terrace_neude with Dissolve(0.5)
    call show_all
    "After visiting the Miffy square, you’re a bit tired, so you decide to have a drink to sit down and rest."
    "There’s a free spot on the terrace."
    "Because of the many canals in the centre, a lot of cafés still receive their beer by boat. In the middle ages, the beer was even brewed by using the water from the canals. Ew!"
    "After a few minutes, a waiter comes to your table."

    # Trivial choice
    label .terrace_drink:
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

        if is_dutch:
            j "\“A [order], please!\”"
        else:
            s "\“A [order], please!\”"
        if friends:
            if is_dutch:
                s "\“For me too, please!\”"
            else:
                j "\“For me too, please!\”"

        "A few moments later, the waiter arrives with [order]."

        if friends:
            # Trivial choice
            label .colour:
                "\“Cheers!\“ you say and you both toast the glasses. As you are both enjoying your drinks, you’re chatting about all kinds of stuff."
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

            label dilemma8A:
                "The topic changes and you talk more about the {i}hospi{/i}."
                if is_dutch:
                    "Sam says that they heard a story from a friend who joined a student house as the only international student."
                else:
                    "Jip says that they heard a story from a friend who joined a student house as the only international student."
                "The house also has a group chat where they chat in Dutch. After the international student was added to the group chat, a few roommates were unsure whether to continue talking in Dutch or switch to English."

                # Consequential choice
                menu:
                    "What would you do?"

                    "Continue in Dutch, highlights in English":
                        $answer8a = "both"
                        $renpy.fix_rollback()
                        if is_dutch:
                            j "\“I would continue casual communication in Dutch, but for important announcements I would switch to English.\”"
                        else:
                            s "\“I would continue casual communication in Dutch, but for important announcements I would switch to English.\”"
                    "Stick to Dutch":
                        $answer8a = "Dutch"
                        $renpy.fix_rollback()
                        $score -= 1
                        if is_dutch:
                            j "\“As I see it, the majority of the house is Dutch. So I would stick to Dutch.\”"
                        else:
                            s "\“As I see it, the majority of the house is Dutch. So I would stick to Dutch.\”"
                    "Switch to English":
                        $answer8a = "English"
                        $renpy.fix_rollback()
                        $score += 1
                        if is_dutch:
                            j "\“I would talk in English. So the international student can read the chat too.\”"
                        else:
                            s "\“I would talk in English. So the international student can read the chat too.\”"

                if is_dutch:
                    s "\“OK, fair. Honestly, I wouldn’t know what I would do. I think it also depends how close the house is and if they’re used to speaking English in their daily lives.\”"
                else:
                    j "\“OK, fair. Honestly, I wouldn’t know what I would do. I think it also depends how close the house is and if they’re used to speaking English in their daily lives.\”"

        if not friends:
            label dilemma8B:
                "As you are enjoying your drink, you see some members of the study association {i}Sticky{/i} are sitting at a table next to you."
                "They’re busy chatting. One member is asked to make an announcement at the next activity."
                "They’re saying that they would rather make the announcement in Dutch, since they're much more comfortable speaking Dutch."
                "However, {i}Sticky{/i} has several international members."

                # Consequential choice
                menu:
                    "If you were in their place, what would you do?"

                    "English summary":
                        $answer8b = "summary"
                        $renpy.fix_rollback()
                        "You would perform the announcement in Dutch and give a highlighted summary in English at the end. That seems fair, right?"
                    "Speak Dutch":
                        $answer8b = "Dutch"
                        $renpy.fix_rollback()
                        $score -= 1
                        "You would perform the announcement in Dutch. That way you can express yourself better and that’s only fair, right?"
                    "Speak English":
                        $answer8b = "English"
                        $renpy.fix_rollback()
                        $score += 1
                        "You would perform the announcement in English. While it costs a little more effort from your side, it’s more important that everybody receives the message loud and clear."


    label dinner:
        "After you finish your drink, your stomach starts rumbling. Time for dinner!"

        # Trivial choice
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

        "The pro of this plan is dinner, but the con is making it. But it’s at least something you like."
        if is_dutch:
            "No way you will make something that has carrots in it. It’s the only thing you despise. But at home, you have to eat what’s on the menu."
        else:
            "No way you will make something that has goat cheese in it. It’s the only thing you despise. But at home, you have to eat what’s on the menu."

        "Because you still need to buy groceries, you open Google Maps to find a supermarket."
        "Plenty of them in the {i}Amsterdamsestraatweg{/i}! This street was built on Napoleon’s orders in 1812 and is part of the route between Paris and Amsterdam."
        "Since it’s the longest shopping street in the Netherlands, finding a supermarket there shouldn’t be too difficult."
        "After you pay, you start walking."

    call supermarket