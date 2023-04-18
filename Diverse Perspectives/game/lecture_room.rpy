label lecture_room:
    scene bg cosmos_lecture with Dissolve(0.5)
    call show_avatar
    "Big, grey letters on the wall spell {i}Cosmos{/i}."
    "That must be the lecture room. You open the door and enter just in time. Quickly, you pick a seat."

    if friends:
        call show_npc
        if is_dutch:
            "Sam sits next to you."
        else:
            "Jip sits next to you."
        call hide_npc

    "The professor starts talking."
    show max at above_right with moveinright
    dr "\“Welcome everybody to your very first class of {i}Introduction to AI{/i}.\”"
    dr "\“I’m dr. Max Caulfield and I hope you all enjoyed your summer break. Let’s start.\”"
    hide max
    "Dr. Caulfield’s monologue continues for a while, but soon your thoughts drift away."
    "You wonder how many international students there are at UU."