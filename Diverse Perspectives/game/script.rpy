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
    $id = renpy.input("What is your participant ID?", allow="0123456789")

    # Give odd participant IDs version A and even IDs version B
    $id = int(id)
    if id % 2  ==  0:
        $versionA = False
        $send_to_file("choices.txt", "\n\n---\n\nVersion B")
    else:
        $versionA = True
        $send_to_file("choices.txt", "\n\n---\n\nVersion A")

    $send_to_file("choices.txt", "\n\nPlayer " + str(id) + "\n")

    # Enter monologue mode
    centered """
    In this game, you will step into the shoes of a student who is about to begin their very first day at Utrecht
    University.

    While you currently stay in a hostel, you’re in desperate need for something more permanent.

    Travelling back and forth is no option, as your hometown is too far away. \n\nFinding a room is not easy peasy lemon
    squeezy...

    Characters and situations are purely fictional. \n\nYour choices affect the outcome of the story. \n\nChoose wisely.

    """
    # Leave monologue mode

    # Go to At Home scene
    call at_home from _call_at_home

    # Write down the total score in a .txt file
    $send_to_file("choices.txt", "\n\nThe total score is " + str(score))

    # This ends the game and returns to the main menu
    return
