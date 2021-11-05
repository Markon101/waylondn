#input your name here
name = input("What is your name? ")

#defines the player name
player_name = name

while True:
#input player class here
    player_class = input("What class are you? ").capitalize()

    #checks to see if player class is a Warrior, Rogue, Mage, or Cleric
    #asks to confirm choice, if not then loops back to re-ask the question
    if player_class in ('Warrior','Rogue','Mage','Cleric'):

        #player class is warrior
        if player_class == 'Warrior':
            print("So, you're a Warrior? ")
            choice = input("y/n? ").capitalize()
            if choice == "Y":
                break

        #player class is rogue
        elif player_class == 'Rogue':
            print("So, you're a Rogue? ")
            choice = input("y/n? ").capitalize()
            if choice == "Y":
                break

        #player class is mage
        elif player_class == 'Mage':
            print("So, you're a Mage? ")
            choice = input("y/n? ").capitalize()
            if choice == "Y":
                break

        #player class is cleric
        elif player_class == 'Cleric':
            print("So, you're a Cleric? ")
            choice = input("y/n? ").capitalize()
            if choice == "Y":
                break

    #otherwise print invalid choice
    else:
        print("Invalid choice!")          
   


#prints and states name and player class
#prints "Welcome to the world of Lindus!"
print(f"Hello, {player_name}. You are a {player_class}.")
print("Welcome to the world of Lindus!")
print("In this world you'll have to make many choices to overcome obstacles within your path.")

#first actual lines of the game
print("You're sitting in a small pub, you see a cloaked stranger sitting alone at a table.")
print("You think to yourself... Why is nobody else noticing him sitting there?")
print("The stranger looks up at you with glaring eyes piercing through you, you look away.")
print("The stranger begins walking towards you reaching for something, what do you do?")

#creates a looping statement in which you make your first real choice
while True:
    choice = input("1. Attack him. 2. Watch to see what he does. ")
    
    #this choice kills the player and stops the game
    if choice == "1":
        print("The stranger vanishes right before your eyes.")
        print("You think to yourself, where did he go?")
        print("You feel a sharp pain through your chest, as the stranger lunges a sword through your heart.")
        break

    #this choice the player receives a map to a dungeon, and the stranger vanishes.
    elif choice == "2":
        print("The stranger reaches out to hand you something.")
        print("It's a map of a dungeon.")
        

        while True:
            #choose yes or no to take the map
            choice = input("Do you take it? Y/N: ").capitalize()

            #if choice is y or Y you take the map
            if choice == "Y":
                print("The stranger hands you the map, he then vanishes in front of your eyes.") 

            #you check out the map
                print("You look down at the map, you wonder if any of this is actually real.")
                print("You pinch yourself, no it's not a dream.")
                print("Then who was that mysterious stranger, and why did he give you a map?")
                break

            #this choice the stranger just vanishes without giving you the map
            elif choice == "N":
                print("The stranger just vanishes right before your eyes.")
                exit()

            #otherwise print invalid choice
            else:
                print("Invalid Choice!")

        #otherwise print invalid choice
        else:
            print("Invalid Choice! ")
        break

    #otherwise print invalid choice        
    else:
        print("Invalid choice!")       

#the story continues further
print("As you study the map closer, you begin to feel some deja vu come over you.")
print("It looks as though you've seen this place before...")
print("It's not far from the land of the undead. That's where you recognize it from.")
print("You attempted to travel there once before, but before you could reach the dungeon you were swarmed by skeletons.")
print("You decide to go asking around about some gear.")

#loopback 
while True:
    choice = input("Would you like to go to the Market or the Garden? ").capitalize()

    #if choice is market
    if choice == "Market":
        print("You decide to take the path down to the old market.")
        print("As you travel further down the path you hear rustling in the bushes.")

        #create loopback here if argument invalid otherwise player dead or you survive
        while True:
            choice = input("Do you want to check it out? Y/N: ").capitalize()
            
            #if choice is yes
            if choice == "Y":
                print("You get closer to the bushes for inspection and see a creature you've never seen before.")
                print("You go to pick it up but it growls loudly at you.")
                print("You decide to back away from the creature.")
                print("You continue down the path and arrive at the market.")
                break

            #if choice is no
            elif choice == "N":
                print("You continue down the path ignoring the rustling sounds.")
                print("All of a sudden something ambushes you!")
                print("It uses a mighty force and throws you against a wall crushing you.")
                exit()
            
            #otherwise error message: invalid choice
            else:
                print("Invalid choice!")
        break

    #if choice is garden
    elif choice == "Garden":
        print("You take the path to the bright gardens.")
        print("Nothing seems to be out of place")
        print("Upon arriving at the gardens you stumble across a knight with a sad look on his face.")
        print("You overhear him speaking of how he has lost his horse.")
        print("You decide to go on a quest to find the horse for the knight.")
        print("He gives you a map with the general area of where the horse was lost circled.")
        print("You decide to leave the garden.")
        break
    
    #otherwise error message: invalid choice
    else:
        print("Invalid choice!")