label supermarket:
    scene bg jumbo with Dissolve(0.5)
    call show_all
    "At the {i}Amsterdamsestraatweg{/i}, you spot a {i}Jumbo{/i}."
    "Although not as cheap as {i}Aldi{/i} or {i}Lidl{/i}, it’s good enough."
    "Standing in the {i}Jumbo{/i}, you put all the ingredients for a [dinner] in your basket."

    if friends:
        label dilemma9:
            if is_dutch:
                j "\“Hey, do you want to eat together? I'm making [dinner]\”"
                s "\“Yes, I would like to! I like everything except goat cheese.\”"
                j "\“Don’t worry, this meal doesn’t have goat cheese.\”"
                s "\“Oh, and I only eat halal meat due to religious reasons.\”"
                j "\“Alright.\”"
            else:
                s "\“Hey, do you want to eat together? I'm making [dinner]\”"
                j "\“Yes, I would like to! I like everything except carrots.\”"
                s "\“Don’t worry, this meal doesn’t have carrots.\”"
                j "\“Oh, and I only eat halal meat due to religious reasons.\”"
                s "\“Alright.\”"

            "You’re both at the supermarket buying ingredients for dinner. However, the halal meat is out of stock."

            # Consequential choice
            menu:
                "What now?"

                "Go to another store to buy it":
                    $answer9 = "halal"
                    $renpy.fix_rollback()
                    $score +=1
                    "Your friend deserves a tasty meal too. You take the extra mile to buy halal meat at another store."
                "Buy regular meat, but pretend it’s halal":
                    $answer9 = "lie"
                    $renpy.fix_rollback()
                    $score -=1
                    "You don’t take your friend's wishes into account. But they don’t need to know that."
                "Just skip the meat":
                    $answer9 = "skip"
                    $renpy.fix_rollback()
                    "You decide to make the dish with less ingredients."
                    "If you don’t buy any ingredients that are not halal, they can’t cheat, right?"

        label dilemma10:
            "After paying for your groceries, you go home and eat dinner together."
            scene bg hostel_lobby with Dissolve(0.5)
            call show_all
            if is_dutch:
                s "\“Thanks for inviting me to your place! I’m staying in a hostel too currently.\”"
                j "\“Yeah, no problem! Wait, in which hostel are you staying?\”"
                s "\“At the Student Hostel close to the city theatre. It’s actually not so far from the Stayokay here at Neude.\”"
                s "\“By the way, can I complain about somebody to you?\”"
                j "\“Of course! Spill the tea.\”"
                s "\“OK, so my friend is vegan, but I just don’t understand why anybody would be vegan.\”"
                s "\“It feels like they do it to guilt-trip people that do eat meat and dairy products. I can’t wrap my head around it.\”"
            else:
                j "\“Thanks for inviting me to your place! I’m staying in a hostel too currently.\”"
                s "\“Yeah, no problem! Wait, in which hostel are you staying?\”"
                j "\“At the Student Hostel close to the city theatre. It’s actually not so far from the Stayokay here at Neude.\”"
                j "\“By the way, can I complain about somebody to you?\”"
                s "\“Of course! Spill the tea.\”"
                j "\“OK, so my friend is vegan, but I just don’t understand why anybody would be vegan.\”"
                j "\“It feels like they do it to guilt-trip people that do eat meat and dairy products. I can’t wrap my head around it.\”"
            "Their monologue of complaints continues for a while."

            # Consequential choice
            menu:
                "What do you do?"

                "Say nothing":
                    $answer10 = "nothing"
                    $renpy.fix_rollback()
                    "Although you don’t think the same about it, you wait until their rant is over."
                    "While tempting, you don’t want to point them out that they have their dietary wishes too."
                "Pretend to agree.":
                    $answer10 = "agree"
                    $renpy.fix_rollback()
                    $score -= 1
                    "You pretend to agree with them and also do your two cents by saying it’s only for the elite and pretentious ones."
                    "Yet in reality, you don’t think that at all, but you don’t want a confrontation."

                    if is_dutch:
                        s "\“Glad you think the same about it. But you don’t have to agree just because we are friends.\”"
                        j "\“I know…\”"
                    else:
                        j "\“Glad you think the same about it. But you don’t have to agree just because we are friends.\”"
                        s "\“I know…\”"

                    # Consequential choice, second chance
                    menu:
                        "What will you do next?"

                        "Keep quiet":
                            $renpy.fix_rollback()
                            "Although you don’t think the same about it, you decide to drop it and finish your plate."
                        "Speak your mind":
                            $renpy.fix_rollback()
                            $score += 1
                            if is_dutch:
                                j "\“Actually, I do disagree. People have their own reasons to be vegan. I think it’s unfair you criticise them for that.\”"
                            else:
                                s "\“Actually, I do disagree. People have their own reasons to be vegan. I think it’s unfair you criticise them for that.\”"
                            call dilemma10_disagree
                "Interrupt them by disagreeing":
                    $answer10 = "disagree"
                    $renpy.fix_rollback()
                    $score += 1
                    "You interrupt them and explain the reasons why people could be vegan."
                    "Your friend shouldn’t criticise them for that, that’s unfair."
                    call dilemma10_disagree

    else:
        "After paying for your groceries, you go home and eat dinner."
        scene bg hostel_lobby with Dissolve(0.5)
        call show_all

    "When you finish eating, it’s almost time to go to the {i}hospi{/i}! You give yourself a pep talk and open the door."
    call at_hospi