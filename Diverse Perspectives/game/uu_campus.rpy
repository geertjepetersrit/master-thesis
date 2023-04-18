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
            "You wonder if they are headed in the same direction as you."
        elif answer2 == "yell":
            if is_dutch:
                s "\“It’s you again! Watch out!\”"
                j "\“Watch out for yourself!\”"
            else:
                j "\“It’s you again! Watch out!\”"
                s "\“Watch out for yourself!\”"
        else:
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