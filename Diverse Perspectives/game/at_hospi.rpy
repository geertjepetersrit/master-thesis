label at_hospi:
    scene bg huize_peereboom with Dissolve(0.5)
    call show_all

    if friends:
        "You go to the {i}hospi{/i} together. This also makes you less nervous, which gives you a good first impression at {i}Huize Peereboom{/i}."
    else:
        "You arrive at the house. You can’t help it, but you’re a little nervous. Or a lot."
        "As you walk through the front door, you see the person you’ve run into earlier today."
        call show_npc
        if score >= 6:
            $score += 1
            "The person greets you kindly and you immediately feel more confident."
        elif score >= 3:
            "The person quickly greets you, but starts talking to someone else."
        else:
            $score -= 1
            "The person ignores you, which makes you even more nervous. This doesn’t help you to make a good first impression."

    scene bg hospi with Dissolve(0.5)
    call show_all
    "You enter the living room and take a seat. There are quite some people and Matilda is here too! Wait, she lives here??"
    "You remember the encounter you had with your potential new roommate earlier today…"
    if friends:
        if is_dutch:
            "You sit next to Sam."
        else:
            "You sit next to Jip."
    else:
        call show_npc
        "You sit next to a familiar face."

    label ending:
        scene bg black with Dissolve(0.5)
        # Good ending
        if score >= 8:
            centered """
            During the day, you’ve become close with the other person. \nYou feel comfortable at the {i}hospi{/i}. {i}Huize Peereboom{/i} likes this.

            At the end of the evening, you get a phone call that you both will be the new roommates! \nThat means no more expensive hostel rooms.

            And you already made a friend on your first day. \nThis day couldn’t get any better!

            """
        # Neutral ending
        elif score >= 4:
            centered """
            You chat a little with the other person and do your best at the {i}hospi{/i}.

            Sadly, neither of you is picked by {i}Huize Peereboom{/i} to be the next roommates.

            At the end of the evening, you both return to your hostel rooms. \nMaybe better luck next time.

            """
        # Bad ending
        else:
            centered """
            The other person acts coldly towards you at the {i}hospi{/i}. This negatively affects you.

            You don’t feel at ease and are therefore not chosen to be the next roommate at {i}Huize Peereboom{/i}. \nInstead, you find out that the other person was chosen.

            You go back to your hostel room and cry yourself to sleep. \nHopefully, not all days will be like this…

            """

        scene bg hostel_room with Dissolve(0.5)
        call show_avatar
        "You close your eyes and fall asleep."

    label recap:
        scene bg black with Dissolve(2)
        centered """
        zzz…

        You’ve reached one of the three endings. \n\nCongratulations for completing the game!

        During the story, there were several dilemmas. \n\nMost of the dilemmas covered a specific diversity (sub)theme.

        Here is a chronological overview of all the (sub)themes that you have possibly encountered:

        Cultural differences: Ethnicity
        \n\nIdentity: Transgender and non-binary people
        \n\nDisabilities: Physical
        \n\nIdentity: Sexual orientation
        \n\nFormal education
        \n\nNeurodivergence
        \n\nCultural differences: Language
        \n\nCultural differences: Religion
        \n\nDietary wishes

        Regarding diversity, this is still the tip of the iceberg. We are all different.

        Although things can be unfamiliar and scary, try to look at them from a diverse perspective. \n\nAnd when you are not sure about something: just ask instead of assume!

        The end. \n\nThank you for playing!
        """