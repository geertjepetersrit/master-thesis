label supermarket:
    scene bg jumbo with Dissolve(0.5)
    call show_all
    "At the {i}Amsterdamsestraatweg{/i}, you spot a {i}Jumbo{/i}."
    "Although not as cheap as {i}Aldi{/i} or {i}Lidl{/i}, it’s good enough."
    "Standing in the {i}Jumbo{/i}, you put all the ingredients for a [dinner] in your basket."

    if friends:
        # Consequential choice
        call dilemma9

        # Consequential choice
        call dilemma10
    else:
        "After paying for your groceries, you go home and eat dinner."
        scene bg hostel_lobby with Dissolve(0.5)
        call show_all

    "When you finish eating, it’s almost time to go to the {i}hospi{/i}! You give yourself a pep talk and open the door."
    call at_hospi