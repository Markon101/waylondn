def funcd():

    # input your name here
    name = input("What is your name? ")

    # defines the player name
    player_name = name

    while True:
        # input player class here
        player_class = input("What class are you? ")

        # checks to see if player class is a Warrior, Rogue, Mage, or Cleric
        # asks to confirm choice, if not then loops back to re-ask the question
        if player_class in ('Warrior', 'Rogue', 'Mage', 'Cleric'):
            # player class is warrior
            if player_class == 'Warrior':
                print("So, you're a Warrior? ")
                choice = input("y/n? ")
                if choice == "y" or choice == "Y":
                    break
            # player class is rogue
            elif player_class == 'Rogue':
                print("So, you're a Rogue? ")
                choice = input("y/n? ")
                if choice == "y" or choice == "Y":
                    break
            # player class is mage
            elif player_class == 'Mage':
                print("So, you're a Mage? ")
                choice = input("y/n? ")
                if choice == "y" or choice == "Y":
                    break
            # player class is cleric
            elif player_class == 'Cleric':
                print("So, you're a Cleric? ")
                choice = input("y/n? ")
                if choice == "y" or choice == "Y":
                    break
        else:
            print("Invalid choice!")


    # prints and states name and player class
    # prints "Welcome to the world of Lindus!"
    print(f"Hello, {player_name}. You are a {player_class}.")
    print("Welcome to the world of Lindus!")
    print("In this world you'll have to make many choices to overcome obstacles within your path.")

    # first actual lines of the game
    print("You're sitting in a small pub, you see a cloaked stranger sitting alone at a table.")
    print("You think to yourself... Why is nobody else noticing him sitting there?")
    print("The stranger looks up at you with glaring eyes piercing through you, you look away.")
    print("The stranger begins walking towards you reaching for something, what do you do?")

    # creates a looping statement in which you make your first real choice
    choice = input("1. Attack him. 2. Watch to see what he does. ")
    # this choice kills the player and stops the game
    if choice == "1":
            print("The stranger vanishes right before your eyes.")
            print("You think to yourself, where did he go?")
            print("You feel a sharp pain through your chest, as the stranger lunges a sword through your heart.")
            return

        # this choice the player receives a map to a dungeon, and the stranger vanishes.
    else:
        print("The stranger reaches out to hand you something.")
        print("It's a map of a dungeon.")
        choice = input("Do you take it? Y/N: ")
        # if choice is y or Y you take the map
        if choice == 'y' or choice == 'Y':
            print("The stranger hands you the map, he then vanishes in front of your eyes.")
            # you check out the map
            print("You look down at the map, you wonder if any of this is actually real.")
            print("You pinch yourself, no it's not a dream.")
            print("Then who was that mysterious stranger, and why did he give you a map?")
            return

            # this choice the stranger just vanishes without giving you the map
            if choice == 'n' or choice == 'N':
                print("The stranger just vanishes right before your eyes.")

    print("As you study the map closer, you begin to feel some deja vu come over you.")