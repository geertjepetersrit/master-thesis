# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Jip", color = "#99ccff")
define s = Character("Sam", color = "#ff99ff")

# Define positions of the characters
transform above_left:
    xanchor 0.0
    yanchor 1.0
    ypos 810
    xpos 100

transform above_right:
    xanchor 1.0
    yanchor 1.0
    ypos 810
    xpos 1820

label at_home:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg hostel_room with fade

    "\[alarm sound beeps\] You wake up and look at your phone."

    label .alarm:
        menu:
            "It’s 8:30 AM, maybe 5 more minutes?"

            "Snooze":
                "You hit the snooze button… zzz …"
                "But 5 minutes later, the ungodly sound wakes you again."
                jump .fixed_alarm
            "Get up":
                jump .fixed_alarm

    label .fixed_alarm: # Lock player's choice
        $renpy.fix_rollback()
        "You stretch your arms and sit up straight in your bed. What day is it?"
        "Oh right, It’s Monday, which means that the summer break has officially ended. Sad."

    label .gender:
        menu:
            "You look around in your hostel room and ask yourself: \“Who do I want to be?\” "

            "Female":
                $gender = "female"
#                 $score += 1
#                 $send_to_file("choices.txt", "Female\n")
                jump .fixed_gender
            "Male":
                $gender = "male"
#                 $send_to_file("choices.txt", "Male\n")
                jump .fixed_gender
            "Non-binary":
                $gender = "nb"
#                 $score -= 1
#                 $send_to_file("choices.txt", "NB\n")
                jump .fixed_gender

    label .fixed_gender: # Lock player's choice
        $renpy.fix_rollback()
        "Then you try to remember more."

    label .country:
        menu:
            "A question pops up in your head: \“What country am I from?\” "

            "the Netherlands":
                $is_dutch = True
#                 $score += 1
#                 $send_to_file("choices.txt", "Dutch\n")
                jump .fixed_country
            "Abroad":
                $is_dutch = False
#                 $score -= 1
#                 $send_to_file("choices.txt", "Abroad\n")
                jump .fixed_country

    label .fixed_country: # Lock player's choice
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

#             show bg hostel_room_blurred
#             j "{i}I'm thinking{\i}."
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

    label .breakfast:
        menu:
            "As you get dressed and prepare for the day, you think: \“What should I eat for breakfast?\” "

            "Bread with {i}hagelslag{\i} (chocolate sprinkles)":
                $breakfast = "hagelslag"
#                 $score += 1
#                 $send_to_file("choices.txt", "Hagelslag\n")
                jump .fixed_breakfast
            "Yoghurt with fruit and muesli":
                $breakfast = "yoghurt"
#                 $send_to_file("choices.txt", "Yoghurt\n")
                jump .fixed_breakfast
            "Nothing":
                $breakfast = "nothing"
#                 $score += -1
#                 $send_to_file("choices.txt", "Nothing\n")
                jump .fixed_breakfast

    label .fixed_breakfast: # Lock player's choice
        $renpy.fix_rollback()

        if breakfast == "hagelslag":
            "Maybe you’ll even add a dot of peanut butter for the sweet tooth. You actually never tried it before, but you’ve heard it’s yummy."
        elif breakfast == "yoghurt":
            "You slice an apple and a banana and put it in a bowl. Then you add the muesli on top. {i}Smakelijk!{\i}"
        else:
            "Skipping breakfast saves time! But you put a snack in your bag to eat later. Lion candy bars are your favourite."

    scene bg hostel_outside with Dissolve(0.5)
#     $send_to_file("choices.txt", "The total score is " + str(score) + "\n")
    return

    label show_avatar:
        if gender == "female":
            show female_avatar at above_left with moveinleft
        elif gender == "male":
            show male_avatar at above_left with moveinleft
        else:
            show nb_avatar at above_left with moveinleft

        return
