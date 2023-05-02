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
            show bg dom_square_blurred with Dissolve(0.5)
            if friends and set_bet and bet == "won":
                if is_dutch:
                    j "\“Wanna bet again?\”"
                    s "\“I’ll skip this one.\”"
                else:
                    s "\“Wanna bet again?\”"
                    j "\“I’ll skip this one.\”"
            if friends and set_bet and bet == "lost":
                if is_dutch:
                    s "\“Wanna bet again?\”"
                    j "\“I’ll skip this one.\”"
                else:
                    j "\“Wanna bet again?\”"
                    s "\“I’ll skip this one.\”"

        show bg dom_square with Dissolve(0.5)
        call dom_height

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
    show bg terrace_neude_blurred with Dissolve(0.5)

    # Trivial choice
    label terrace_drink:
        call drink_order

        if is_dutch:
            j "\“A [order], please!\”"
        else:
            s "\“A [order], please!\”"
        if friends:
            if is_dutch:
                s "\“For me too, please!\”"
            else:
                j "\“For me too, please!\”"

        show bg terrace_neude with Dissolve(0.5)
        "A few moments later, the waiter arrives with [order]."

        if friends:
            # Trivial choice
            call colour
            call dilemma8A

        if not friends:
            call dilemma8B

    label dinner:
        show bg terrace_neude with Dissolve(0.5)
        "After you finish your drink, your stomach starts rumbling. Time for dinner!"

        # Trivial choice
        call dinner_choice

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