#input your name here
name = input("What is your name? ")

#defines the player name
player_name = name

while True:
#input player class here
    player_class = input("What class are you? ")

    #checks to see if player class is a Warrior, Rogue, Mage, or Cleric
    #asks to confirm choice, if not then loops back to reask the question
    if player_class in ('Warrior','Rogue','Mage','Cleric'):
        if player_class == 'Warrior':
            print("So, you're a Warrior? ")
            choice = input("y/n? ")
            if choice == "y":
                break

        elif player_class == 'Rogue':
            print("So, you're a Rogue? ")
            choice = input("y/n? ")
            if choice == "y":
                break

        elif player_class == 'Mage':
            print("So, you're a Mage? ")
            choice = input("y/n? ")
            if choice == "y":
                break

        elif player_class == 'Cleric':
            print("So, you're a Cleric? ")
            choice = input("y/n? ")
            if choice == "y":
                break
    else:
        print("Invalid choice!")          
   


#prints and states name and player class
#prints "Welcome to the world of Lindus!"
print(f"Hello, {player_name}. You are a {player_class}.")
print("Welcome to the world of Lindus!")