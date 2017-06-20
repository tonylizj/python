
# -------------------------------------------------------------------------------
# Name:		adventure_game_tonyli.py
# Purpose:		an adventure game where you are stuck in a stranded spaceship
#
# Author:		Li.T
#
# Created:		20/6/2017
# ------------------------------------------------------------------------------


# import modules
import time
import os
import random


def cls():
    """
    Clears console screen
    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def cleaninput(text):
    """
    Changes text to lowercase and removes spaces
    :param text: text to clean
    :return: cleaned text
    """
    # changes text to a list of lowercase letters
    text_list = list(text.lower())
    # remove spaces
    for letter in range(len(text_list)):
        if text_list[letter] == " ":
            text_list[letter] = ""

    # returns joined text
    return "".join(text_list)


def interpretinput(text):
    """
    Changes movement words to "n", "s", "e", or "w"
    :param text: movement command
    :return: movement letter or invalid
    """
    # cleans text
    text = cleaninput(text)
    # changes directions to a single letter
    if text in ["north", "n"]:
        return "n"

    elif text in ["south", "s"]:
        return "s"

    elif text in ["east", "e"]:
        return "e"

    elif text in ["west", "w"]:
        return "w"

    # returns invalid if the user did not enter a direction
    else:
        return "invalid"


class Room:
    def __init__(self, number, name, description, actions):
        """
        Initialized room object with number, name, description, and actions
        :param number: number of room
        :param name: name of room
        :param description: description of room
        :param actions: possible actions of room
        """
        self.number = number
        self.name = name
        self.description = description
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.actions = actions

    def set_directions(self, north, south, east, west):
        """
        Sets rooms that connect to a room object
        :param north: room to the north of room
        :param south: room to the south of room
        :param east: room to the east of room
        :param west: room to the west of room
        :return: None
        """
        # sets direction methods
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def move(self):
        """
        Moves player to a connected room
        :return: new room player is in
        """
        while True:
            # changes direction to single letter
            direction = interpretinput(input("\nWhere do you go? "))
            # returns the room in the specified direction in relation to the current room
            if direction == "n" and self.north != None:
                return self.north

            elif direction == "s" and self.south != None:
                return self.south

            elif direction == "e" and self.east != None:
                return self.east

            elif direction == "w" and self.west != None:
                return self.west

            # returns the unchanged room if the movement is invalid
            elif direction == "invalid":
                print("\nInvalid direction.")

            else:
                print("There is no room in that direction.")


# room definitions
room0 = Room(0, "airlock",
             "You walk into the airlock, the sealing of the door is partially bent from the crash.\nThere is a corridor to the south.",
             ("Look outside", "Go outside"))
room1 = Room(1, "shipmanage",
             "You are at the ship management sector. Thousands of switches and indicators line the walls.\nCommunications is to the south and driving is to the east.",
             ("Check ship status", "Take extinguisher"))
room2 = Room(2, "driving",
             "You are at the ship's driving controls. It appears to be intact.\nThe engineering station is to the south and ship management is to the west.",
             ("Try to jump",))
room3 = Room(3, "airlockhallway",
             "You walk into the corridor to the airlock. The secondary cannon is stationed by the wall.\nThe airlock is to the north and weapons control is to the south.",
             ("Take spacesuits", "Repair secondary cannon"))
room4 = Room(4, "communications",
             "You are at the ship's communications systems. They are broken beyond repair.\nShip management is to the north, there is a hallway to the south, the engineering station is to the east.",
             ("Save game",))
room5 = Room(5, "engineerstation",
             "You are at the station of the chief engineer. Much of his work is scattered all over the table.\nDriving controls are to the north and communications is to the west.",
             ("Search through blueprints.",))
room6 = Room(6, "weapons",
             "You arrive at the ship's weapons management. The main cannon is stationed here.\nThe hallway to the airlock is to the north and a corridor is to the east.",
             ("Repair primary cannon", "Take pistol"))
room7 = Room(7, "corridor",
             "You continue walking down the corridor.\nWeapons control is to the west while the corridor extends east.",
             ("Keep going",))
room8 = Room(8, "corridor",
             "You walk into a corridor.\nCommunications is to the north while the corridor branches to the west and south",
             ("Keep going",))
room9 = Room(9, "corridor",
             "You continue walking into another corridor.\nThis corridor extends to the north, the dock is to the south.",
             ("Keep going",))
room10 = Room(10, "debris",
              "You reach the end of the hallway. What used to extend into the library is now a pile of rubble and debris. You notice a piece of newspaper on the ground.\nA corridor is to the east.",
              ("Take newspaper",))
room11 = Room(11, "corridor", "You walk into a corridor.\nThe dock is to the east and a pile of debris is to the west.",
              ("Keep going",))
room12 = Room(12, "dock",
              "You are at the dock. This is where your ship would dock onto others to receive or give supplies.\nThere are corridors to the north, east, and west. The primary airlock is to the south.",
              ("Keep going",))
room13 = Room(13, "corridor",
              "You walk into a corridor, there is a strong smell of fire.\nThe dock is to the west and the navigations room is to the east.",
              ("Keep going",))
room14 = Room(14, "navsystem",
              "You arrive at the navigations room. The autonavigator is on fire. You must put it out.\nThere is a corridor to the west.",
              ("Put out fire",))
room15 = Room(15, "primary airlock",
              "You walk into the primary airlock. This airlock was not designed for crew, but for the transportation of supplies.\nThe dock is to the north.",
              ("Look outside",))

# room connection definitions
room0.set_directions(None, room3, None, None)
room1.set_directions(None, room4, room2, None)
room2.set_directions(None, room5, None, room1)
room3.set_directions(room0, room6, None, None)
room4.set_directions(room1, room8, room5, None)
room5.set_directions(room2, None, None, room4)
room6.set_directions(room3, None, room7, None)
room7.set_directions(None, None, room8, room6)
room8.set_directions(room4, room9, None, room7)
room9.set_directions(room8, room12, None, None)
room10.set_directions(None, None, room11, None)
room11.set_directions(None, None, room12, room10)
room12.set_directions(room9, room15, room13, room11)
room13.set_directions(None, None, room14, room12)
room14.set_directions(None, None, None, room13)
room15.set_directions(room12, None, None, None)


def victory(inventory):
    """
    Prints out victory message
    :param inventory: list of player's possessions
    :return: None
    """
    # prints victory
    print(" __      _______ _____ _______ ____  _______     __")
    print(" \ \    / /_   _/ ____|__   __/ __ \|  __ \ \   / /")
    print("  \ \  / /  | || |       | | | |  | | |__) \ \_/ / ")
    print("   \ \/ /   | || |       | | | |  | |  _  / \   /  ")
    print("    \  /   _| || |____   | | | |__| | | \ \  | |   ")
    print("     \/   |_____\_____|  |_|  \____/|_|  \_\ |_|   ")
    print("                                                   ")

    # counts the number of cannons the player fixed
    cannons = 0
    if "cannon1" in inventory:
        cannons += 1

    if "cannon2" in inventory:
        cannons += 1

    # prints the victory message with cannons repaired
    print("Congratulations. You repaired navigations and arrived home, evading Federation forces.")
    print("You also repaired {0} cannon(s) out of 2.".format(cannons))
    quit()


def battle(inventory):
    """
    Fights player and federation soldiers
    :param inventory: list of player's possessions
    :return: whether the player died
    """
    # if the player's ship is being raided
    if "raid" in inventory:
        # 40% chance to spawn an enemy
        spawn = random.randint(0, 5)
        if spawn < 3:
            # if the player has a pistol
            if "pistol" in inventory:
                print("\nYou suddenly see face-to-face to a Federation soldier. You pull out the pistol you took from weapons management.\n")
                time.sleep(3)
                damage = random.randint(5, 10)
                # health is reduced by the amount of damage taken
                inventory[0] = inventory[0] - damage
                print("You took {0} points of damage. You have {1} health remaining.".format(damage, inventory[0]))

            # if the player did not take the pistol
            elif "pistol" not in inventory:
                print("\nYou suddenly see face-to-face to a Federation soldier. You pull out your knife.")
                print("There is a pistol at weapons management. It would help.\n")
                time.sleep(3)
                damage = random.randint(10, 20)
                # health is reduced by the amount of damage taken
                inventory[0] = inventory[0] - damage
                print("You took {0} points of damage. You have {1} health remaining.".format(damage, inventory[0]))

            # if health is below zero, return True
            if inventory[0] <= 0:
                return True

            # otherwise return False
            else:
                return False

    # if the player is not being raided for the enemy does not spawn, nothing happens
        else:
            pass

    else:
        pass


def performaction(currentroom, action, inventory):
    """
    Performs actions described in room object
    :param currentroom: room player is in
    :param action: action player chose
    :param inventory: list of player's possessions
    :return: inventory
    """
    # checks for the room the player is in
    if currentroom == room0:
        # checks for which action the player chose
        if action == "1":
            print("You stare into the abyss..")

        elif action == "2":
            # checks for item in player's inventory
            if "spacesuit" in inventory:
                print("You put on the spacesuit and head outside. There is an apparent coldness but you are protected by the suit.\nAsteroids drift by, sometimes knocking into your ship and producing heart-wrenching sounds. You see ship systems broken from the accident, electricity flickering in the darkness.")
                if "navbp" not in inventory:
                    print("You notice a piece of paper floating just outside of your ship. It's the navigations blueprint! You snatch it quickly.")
                    # adds item to player's inventory
                    inventory.append("navbp")

                else:
                    print("This is where you found the navigations blueprint.")

            else:
                print("You have no spacesuit.")

        elif action == "":
            print("You choose to do nothing.")

        else:
            print("Invalid input.")

    elif currentroom == room1:
        if action == "1":
            print("We seem to be stranded in an asteroid belt. Most of the ship's left wing has been destroyed and the right wing is on fire. All other sectors only took minor damage.")
            print("Both of the ship's cannons have been damaged and navigations is no longer working. You will need to repair these systems if you want to head home.")

        elif action == "2":
            if "extinguisher" not in inventory:
                inventory.append("extinguisher")
                print("You take the fire extinguisher. It could be useful.")

            else:
                print("You already have the extinguisher.")

        elif action == "":
            print("You choose to do nothing.")

        else:
            print("Invalid input.")

    elif currentroom == room2:
        if action == "1":
            if "nav" in inventory:
                print("The navigations system is working. The ship is ready to jump.")
                print("Once you begin travelling home, you will no longer be able to repair any cannons.")
                askjump = input("Jump anyway? (y/n) ")
                if askjump == "y":
                    # prints victory message
                    victory(inventory)

                elif askjump == "n":
                    print("You choose not to jump.")

                else:
                    print("Invalid input.")

            else:
                print("You pull back the lever and release it. However, the ship does not budge.")
                print("You should check ship management to see what's going on.")

        elif action == "":
            print("You choose to do nothing.")

        else:
            print("Invalid input.")

    elif currentroom == room3:
        if action == "1":
            if "spacesuit" not in inventory:
                inventory.append("spacesuit")
                print("You unhook the spacesuit and try it on. It seems to be your size.")

            else:
                print("You already have the spacesuit.")

        elif action == "2":
            if "cannon2bp" in inventory:
                inventory.append("cannon2")
                print("Turns out it was just missing a few screws. You pick them up from the floor and get the secondary cannon working by following the blueprint.")

            else:
                print("This system is too complicated for you to fix. You will need to find a blueprint. Joe, who always liked reading newspapers, also liked this blueprint. Weird.")

        elif action == "":
            print("You choose to do nothing.")

        else:
            print("Invalid input.")

    elif currentroom == room4:
        if action == "1":
            # saves game
            savefile = open("tonyli_gamesave.txt", "w")
            # writes player's inventory to save file
            for item in inventory:
                savefile.write(str(item) + "\n")
            savefile.close()
            print("Game saved.")

        elif action == "":
            print("You choose to do nothing.")

        else:
            print("Invalid input.")

    elif currentroom == room5:
        if action == "1":
            if "cannon1bp" not in inventory:
                inventory.append("cannon1bp")
                print("You find the blueprint for the ship's main cannon, taking it with you.")

            else:
                print("There are no more useful blueprints.")

        elif action == "":
            print("You choose to do nothing.")

        else:
            print("Invalid input.")

    elif currentroom == room6:
        if action == "1":
            if "cannon1bp" in inventory:
                inventory.append("cannon1")
                print("With the primary cannon blueprint, you effortlessly repair it.")

            else:
                print("You will need the blueprint to fix this system. The engineer should have it around his station.")

        elif action == "2":
            if "pistol" in inventory:
                print("You already took the pistol.")

            else:
                inventory.append("pistol")
                print("You take the pistol. Just in case.")

        elif action == "":
            print("You choose to do nothing.")

        else:
            print("Invalid input.")

    elif currentroom == room7:
        if action == "1":
            print("You straighten your back and keep walking. The fate of this ship is at stake.")

        elif action == "":
            print("You choose to do nothing.")

        else:
            print("Invalid input.")

    elif currentroom == room8:
        if action == "1":
            print("You remember sitting down by the table here, playing cards with your commander. You keep going.")

        elif action == "":
            print("You choose to do nothing.")

        else:
            print("Invalid input.")

    elif currentroom == room9:
        if action == "1":
            print("This is the center of the ship. You keep going.")

        elif action == "":
            print("You choose to do nothing.")

        else:
            print("Invalid input.")

    elif currentroom == room10:
        if action == "1":
            if "cannon2bp" not in inventory:
                inventory.append("cannon2bp")
                print("You pick up the newspaper. The declaration of war is on the front page, reminding you of your duty.")
                print("You notice, tucked inside the sports section, the blueprint for the secondary cannon. You blame Joe for this")

            else:
                print("This is where you got the secondary cannon blueprint.")

        elif action == "":
            print("You choose to do nothing.")

        else:
            print("Invalid input.")

    elif currentroom == room11:
        if action == "1":
            print("This used to be your favourite hallway because of the smell of the books. You keep going.")

        elif action == "":
            print("You choose to do nothing.")

        else:
            print("Invalid input.")

    elif currentroom == room12:
        if action == "1":
            print("The dock would usually be busy, however, the ship is frighteningly quiet. You keep going.")

        elif action == "":
            print("You choose to do nothing.")

        else:
            print("Invalid input.")

    elif currentroom == room13:
        if action == "1":
            print("There is the flickering of flames at the end of the corridor, you fear the worst. You keep going.")

        elif action == "":
            print("You choose to do nothing.")

        else:
            print("Invalid input.")

    elif currentroom == room14:
        if action == "1":
            if "extinguisher" in inventory:
                if "fireout" in inventory:
                    print("You realize that you have already put out the fire. It was just a hallucination.")
                    if "nav" in inventory:
                        print("The navigation system is working.")

                    else:
                        if "navbp" in inventory:
                            inventory.append("nav")
                            print("You fix the navigations system with the blueprint you found. It works.")
                            time.sleep(1)
                            print("Let's go home.")
                            time.sleep(2)

                        else:
                            print(
                                "You need to find the blueprint for navigations to fix this. Somebody jokingly said that he would throw it into space..")

                else:
                    inventory.append("fireout")
                    print(
                        "You spray the extinguisher all over the room, putting the fire out. Luckily, the navigation system is not damaged.")
                    if "navbp" in inventory:
                        inventory.append("nav")
                        print("You fix the navigations system with the blueprint you found. It works.")
                        time.sleep(1)
                        print("Let's go home.")
                        time.sleep(2)

                    else:
                        print(
                            "You need to find the blueprint for navigations to fix this. Somebody jokingly said that he would throw it into space..")

            else:
                print("You need to find a fire extinguisher. There should be one at ship management.")

            if "raid" not in inventory:
                inventory.append("raid")
                print("\nSuddenly, the whole ship shakes. Another ship has docked with your ship. Judging by the signature, it's a Federation ship. How could they have found us?")
                print("Federation soldiers are piling into the ship. You need to be careful.")

        elif action == "":
            print("You choose to do nothing.")

        else:
            print("Invalid input.")

    elif currentroom == room15:
        if action == "1":
            print("You can see asteroids moving in the darkness. A faint glow in the distance resembles a Federation ship in pursuit. You should hurry.")

        elif action == "":
            print("You choose to do nothing.")

        else:
            print("Invalid input.")

    # returns inventory
    return inventory


def intro(inventory):
    """
    Shows title and let's player load game or start a new game
    :param inventory: list of player's possessions
    :return: inventory
    """
    # prints game title
    print("  _      _____ _____ _    _ _______ _____ _____  ______ ______ _____  ")
    print(" | |    |_   _/ ____| |  | |__   __/ ____|  __ \|  ____|  ____|  __ \ ")
    print(" | |      | || |  __| |__| |  | | | (___ | |__) | |__  | |__  | |  | |")
    print(" | |      | || | |_ |  __  |  | |  \___ \|  ___/|  __| |  __| | |  | |")
    print(" | |____ _| || |__| | |  | |  | |  ____) | |    | |____| |____| |__| |")
    print(" |______|_____\_____|_|  |_|  |_| |_____/|_|    |______|______|_____/   Version 1.13")
    print("                                                                        Created by: Tony Li")
    print("                             1: New Game")
    print("                             2: Load Game")

    while True:
        gameoption = input("\n\nEnter an option: ")
        # plays story if the player selects new game
        if gameoption == "1":
            cls()
            print("\n\n\n\n")
            print(
                "After 11 years serving aboard the RS Conqueror, the Second War of Jupiter has finally come to a close.")
            time.sleep(4)
            print("It's time to head home.")
            time.sleep(2)
            print("\n\"Prepare to jump!\", the captain shouts over the roar of the ion engines. I ready the propellant.")
            time.sleep(3)
            print("\n\"10\"")
            time.sleep(1)
            print("\"9\"")
            time.sleep(1)
            print("\"8\"")
            time.sleep(1)
            print("\"7\"")
            time.sleep(1)
            print("\"6\"")
            time.sleep(1)
            print("\"5\"")
            time.sleep(1)
            print("\"4\"")
            print("\"The coolant!\", the sergeant yells. \"Where is it?!\"")
            time.sleep(1)
            print("\"3\"")
            time.sleep(1)
            print("\"2\"")
            time.sleep(1)
            print("\"1\"")
            print("\"I've got it!\". The chief engineer appears, sprinting towards the bridge. \"Hurry-")
            time.sleep(1)
            print("\"Jump!\"")
            time.sleep(4)
            cls()
            print("\n\nThe engineer's voice is cut short as the ship shoots out into space..")
            time.sleep(2)
            print("\nYou wake up to the ship's alarms.")
            time.sleep(2)
            input("Press enter to begin..")
            return inventory

        # loads from save file if the player selects load game
        elif gameoption == "2":
            try:
                savefile = open("tonyli_gamesave.txt", "r")
                # loads file text into player inventory
                while True:
                    inventory.append(savefile.readline().strip())
                    if inventory[-1] == "":
                        inventory.remove("")
                        inventory.remove(100)
                        break

                print("\nGame loaded.")
                inventory[0] = int(inventory[0])
                print("Inventory:")
                for i in range(len(inventory)):
                    print(inventory[i], end=' ')
                return inventory

            # if ther save file doesn't exist
            except FileNotFoundError:
                print("No save file found.")

        # if the player did not type 1 or 2
        else:
            print("Invalid option.")
            time.sleep(1)
            cls()
            print("\n\n")


def playgame():
    """
    Main function that manages gameplay
    :return: None
    """
    # sets starter room and health
    currentroom = room2
    inventory = [100]
    gameover = False

    # plays intro
    inventory = intro(inventory)

    # main loop
    while not gameover:
        # prints room description
        print("\n----------------------------------------------\n\n" + currentroom.description + "\n")

        # lists choices
        for i, action in enumerate(currentroom.actions):
            print("{0}: {1}".format(i + 1, action))

        # executes action, performs movement, does battle
        print("Press enter to do nothing.")
        chosenaction = input("\nWhat do you do? ")
        print()
        inventory = performaction(currentroom, chosenaction, inventory)
        time.sleep(1)
        currentroom = currentroom.move()
        gameover = battle(inventory)
        input("Press enter to continue..")

    # if the player dies
    print(" __     ______  _    _   _____ _____ ______ _____  ")
    print(" \ \   / / __ \| |  | | |  __ \_   _|  ____|  __ \ ")
    print("  \ \_/ / |  | | |  | | | |  | || | | |__  | |  | |")
    print("   \   /| |  | | |  | | | |  | || | |  __| | |  | |")
    print("    | | | |__| | |__| | | |__| || |_| |____| |__| |")
    print("    |_|  \____/ \____/  |_____/_____|______|_____/ ")
    print("                                                   ")

# begins game
playgame()
