name = input("What is your name? ")
player_name = name
player_class = input("What class are you? ")

if player_class in ('Warrior','Rogue','Mage','Cleric'):
        if player_class == 'Warrior':
            print("So, you're a Warrior? ")
            input("y/n? ")

        elif player_class == 'Rogue':
            print("So, you're a Rogue? ")
            input("y/n? ")

        elif player_class == 'Mage':
            print("So, you're a Mage? ")
            input("y/n? ")    

        elif player_class == 'Cleric':
            print("So, you're a Cleric? ")
            input("y/n? ")
else:
    print("Invalid choice!")     

print(f"Hello, {player_name}")
print(f"Hello, {player_name}. You are a {player_class}.")