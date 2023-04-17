# The script of the game goes in this file.
# The game starts here.

# Create a .txt file to write down the player's choices
init python:

    def send_to_file(filename, text):
        with open(config.gamedir + "/" + filename, "a") as f:
            f.write(text)
            f.close()
        return

label start:

    $score = 0
#   $send_to_file("choices.txt", "The total score is " + str(score) + "\n")

    # Enter monologue mode
    centered """
    In this game, you will step into the shoes of a student who is about to begin their very first day at Utrecht
    University.

    While you currently stay in a hostel, you’re in desperate need for something more permanent.

    Travelling back and forth is no option, as your hometown is too far away. Finding a room is not easy peasy lemon
    squeezy...

    Characters and situations are purely fictional. Your choices affect the outcome of the story. Choose wisely.

    """
    # Leave monologue mode

    # Go to At Home scene
    call at_home

    # This ends the game and returns to the main menu
    return

# TODO: add blurry backgrounds when characters are talking
