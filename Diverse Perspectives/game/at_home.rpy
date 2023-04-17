

label at_home:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg hostel_room with Dissolve(0.5)

    "\[alarm sound beeps\] You wake up and look at your phone."

    # Trivial choice
    label .alarm:
        menu:
            "It’s 8:30 AM, maybe 5 more minutes?"

            "Snooze":
                $renpy.fix_rollback()
                "You hit the snooze button… zzz …"
                "But 5 minutes later, the ungodly sound wakes you again."
            "Get up":
                $renpy.fix_rollback()


    "You stretch your arms and sit up straight in your bed. What day is it?"
    "Oh right, It’s Monday, which means that the summer break has officially ended. Sad."

    # Trivial choice
    label .gender:
        menu:
            "You look around in your hostel room and ask yourself: \“Who do I want to be?\” "

            "Female":
                $gender = "female"
                $renpy.fix_rollback()
            "Male":
                $gender = "male"
                $renpy.fix_rollback()
            "Non-binary":
                $gender = "nb"
                $renpy.fix_rollback()

    "Then you try to remember more."

    # Trivial choice
    label .country:
        menu:
            "A question pops up in your head: \“What country am I from?\” "

            "the Netherlands":
                $is_dutch = True
                $renpy.fix_rollback()
            "Abroad":
                $is_dutch = False
                $renpy.fix_rollback()

    "It all comes back to you now. Your name is..."

    if is_dutch:
        call show_avatar
        "Jip and today is your first day at Utrecht University."
        "While you have visited several universities on many open days, Utrecht is all you wanted."
        "The city has something magical. While it has canals like Amsterdam, it’s smaller and thus more cosy. However, with over 360,000 inhabitants, Utrecht is not small."
        "In 1808, Napoleon’s brother made Utrecht even the capital city! However, that didn’t last long, as Amsterdam regained that position."
        "Although in high school the science courses were not easy, you’re eager to start studying Artificial Intelligence."
        "As you’re in your early 20s, you also can’t wait to live on your own and have your parents out of your hair. It’s about time."
        "The only downside of moving to Utrecht will be that you have to leave Stitch behind, your precious cat."
    else:
        call show_avatar
        "Sam and today is your first day at Utrecht University."
        "After carefully researching options for studying abroad, Utrecht stood out for you."
        "The city has something magical. While it has canals like Amsterdam, it’s smaller and thus more cosy. However, with over 360,000 inhabitants, Utrecht is not small."
        "In 1808, Napoleon’s brother made Utrecht even the capital city! However, that didn’t last long, as Amsterdam regained that position."
        "Although in high school the science courses were not easy, you’re eager to start studying Artificial Intelligence."
        "As you’re in your early 20s, you also can’t wait to live on your own and have your parents out of your hair. It’s about time."
        "The only downside of moving to Utrecht will be that you have to leave Stitch behind, your precious cat."

    "You get out of your bed and open your suitcase for some clothes. Yeah, that outfit will do."

    scene bg hostel_lobby with Dissolve(0.5)
    call show_avatar

    # Trivial choice
    label .breakfast:
        menu:
            "As you get dressed and prepare for the day, you think: \“What should I eat for breakfast?\” "

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

    # Go to Travelling scene
    call travelling