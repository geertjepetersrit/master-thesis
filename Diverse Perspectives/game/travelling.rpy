label travelling:
    scene bg hostel_outside with Dissolve(0.5)
    call show_avatar from _call_show_avatar_15

    "After brushing your teeth and grabbing your backpack, it’s time to go to the campus. You go through the door and leave the hostel."
    "As you close your eyes, you think about your day."

    scene bg black with Dissolve(0.5)

    centered """
    While you are glad you have a place to stay for now, you would rather find housing for a longer period of time. Preferable with more space, but less expensive. \n\nLuckily, this evening you are invited for a {i}hospiteeravond{/i}.

    You wonder how the evening will play out. \n\nBasically, you are invited to a house viewing, which is called a {i}hospi{/i}, in short. The house is looking for new roommates.

    Usually, several people are invited and you have the chance to see the house and the room. \n\nA small party can be held, but in the end, it is all about who is the best match for the house.

    Or in this case: two matches, as there are two rooms available. \n\n{i}Huize Peereboom{/i} is looking for one Dutch and one international student, to maintain the balance.

    Likewise, {i}Huize Peereboom{/i} finds it important that everyone gets along well, so they prefer Dutch and international students who are already close.

    So, it seems to be in your benefit to befriend someone from a different nationality. \n\nAlso, you could try to interact with strangers too, as both could increase your chances of getting a room. \n\nYou never know when you will run into your potential roommates…

    """

    scene bg hostel_outside with Dissolve(0.5)
    call show_avatar from _call_show_avatar_16

    if is_dutch:
        "You already imagine how it would be if you’d live there. Will your new roommates be as excited as you about playing card games?"
        "{i}Ligretto{/i} is your favourite, but you also enjoy playing {i}Saboteur{/i}."
    else:
        "You already imagine how it would be if you’d live there. Decorating your room with cute plants from that Dutch garden store-- what was it called again?"
        "{i}The Inner Time? The Intratuin?{/i} Anyway, you’re looking forward to it. Your room at home is full with pancake plants."

    "A notification from your phone brings you back to the present. You should leave now or you’ll be late!"

    # Trivial choice
    call transport from _call_transport

    if by_bike:
        scene bg bike with Dissolve(0.5)
        call show_avatar from _call_show_avatar_17
        "You find your keys, unlock your bike and hop on it. Just go with the flow. There is no other city in the Netherlands that has as many cyclists as Utrecht."
        "The traffic is quite overwhelming during rush hour and your top priority is not crashing into anyone or anything. Easier said than done…"
        "While you are waiting for a red light…"
        call dilemma1 from _call_dilemma1
    else:
        scene bg bus_inside with Dissolve(0.5)
        call show_avatar from _call_show_avatar_18
        "You grab your OV-card and head to the nearest bus station. The bus you take has the size of three regular buses, being 25 metres long. Woah!"
        "Luckily, you find a spot that’s free. On the bus…"
        call dilemma1 from _call_dilemma1_1

    call uu_campus from _call_uu_campus