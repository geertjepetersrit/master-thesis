# The script of the game goes in this file.

# The game starts here.

label start:

    $score = 0

    # Narrative intro

    centered "In this game, you will step into the shoes of a student who is about to begin their very first day at Utrecht University."
    centered "While you currently stay in a hostel, you’re in desperate need for something more permanent."
    centered "Travelling back and forth is no option, as your hometown is too far away. Finding a room is not easy peasy lemon squeezy..."
    centered "Characters and situations are purely fictional. Your choices affect the outcome of the story. Choose wisely."

    call at_home

    # This ends the game.

    return
