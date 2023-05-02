

label at_home:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg hostel_room with Dissolve(0.5)

    "\[alarm sound beeps\] You wake up and look at your phone."

    # Trivial choice
    call alarm

    "You stretch your arms and sit up straight in your bed. What day is it?"
    "Oh right, It’s Monday, which means that the summer break has officially ended. Sad."

    # Trivial choice
    call gender

    "Then you try to remember more."

    # Trivial choice
    call country

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
    call breakfast

    # Go to Travelling scene
    call travelling