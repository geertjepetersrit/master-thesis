# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Jip", color = "#99ccff")
define s = Character("Sam", color = "#ff99ff")

# Define positions of the characters

transform above_left:
    xanchor 0.0
    yanchor 1.0
    ypos 810
    xpos 0

transform above_right:
    xanchor 1.0
    yanchor 1.0
    ypos 810
    xpos 1920

label at_home:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene hostel_room with fade

    "\[alarm sound beeps\] You wake up in your hostel room. Oh right, summer break has officially ended."

    label .gender:
        menu:
            "You look around and ask yourself: \“Who do I want to be?\” "

            "Female":
                $gender = "female"
                jump .fixed_gender
            "Male":
                $gender = "male"
                jump .fixed_gender
            "Non-binary":
                $gender = "nb"
                jump .fixed_gender


    # TODO: extend this
    #     if gender == "female":
    #         # Show female avatar
    #     elif gender == "male":
    #         # Show male avatar
    #     else:
    #         # Show non-binary avatar

    label .fixed_gender: # Lock player's choice
        $renpy.fix_rollback()
        "Then you try to remember more."

    label .country:
        menu:
            "A question pops up in your head: \“What country am I from?\” "

            "the Netherlands":
                $is_dutch = True
                $score += 1
                jump .fixed_country
            "Abroad":
                $is_dutch = False
                $score -= 1
                jump .fixed_country

    label .fixed_country: # Lock player's choice
        $renpy.fix_rollback()

        "It all comes back to you now. Your name is..."

        if is_dutch:
            show dutch_avatar at above_left with moveinleft
            "Jip and today is your first day at Utrecht University."
            "While you have visited several universities on many open days, Utrecht is all you wanted."
            j "{i}I'm thinking{\i}."
        else:
            show international_avatar at above_left with moveinleft
            "Sam and today is your first day at Utrecht University."
            "After carefully researching options for studying abroad, Utrecht stood out for you."

    scene hostel_lobby with Dissolve(0.5)

    label .breakfast:
        menu:
            "As you get dressed and prepare for the day, you think: \“What should I eat for breakfast?\” "

            "Bread with {i}hagelslag{\i} (chocolate sprinkles)":
                $breakfast = "hagelslag"
                $score += 1
                jump .fixed_breakfast
            "Yoghurt with fruit and muesli":
                $breakfast = "yoghurt"
                jump .fixed_breakfast
            "Nothing":
                $breakfast = "nothing"
                $score += -1
                jump .fixed_breakfast

    label .fixed_breakfast: # Lock player's choice
        $renpy.fix_rollback()

        if breakfast == "hagelslag":
            "Maybe you’ll even add a dot of peanut butter for the sweet tooth."
        elif breakfast == "yoghurt":
            "You slice an apple and a banana and put it in a bowl."
        else:
            "Skipping breakfast saves time! But you put a snack in your bag to eat later."

    scene hostel_outside with Dissolve(0.5)
    "Total score is [score]"