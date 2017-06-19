import time
import os


def cleaninput(text):
    text_list = list(text.lower())
    for letter in range(len(text_list)):
        if text_list[letter] == " ":
            text_list[letter] = ""

    return "".join(text_list)


def interpretinput(text):
    cleaninput(text)
    if text == "help":
        pass

    elif text in ["north", "n"]:
        return "n"

    elif text in ["south", "s"]:
        return "s"

    elif text in ["east", "e"]:
        return "e"

    elif text in ["west", "w"]:
        return "w"

    else:
        return "invalid"


class Room:

    def __init__(self, number, name, description, actions):
        self.number = number
        self.name = name
        self.description = description
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.actions = actions

    def set_directions(self, north, south, east, west):
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def move(self, direction):
        direction = interpretinput(direction)
        if direction == "n" and self.north != None:
            return self.north

        if direction == "s" and self.south != None:
            return self.south

        if direction == "e" and self.east != None:
            return self.east

        if direction == "w" and self.west != None:
            return self.west

        if direction == "invalid":
            print("Invalid direction.")
            return self

room0 = Room(0, "room0", "You walk into the airlock, airtight suits are hung by the walls.", ("Look outside", "Go outside", "Do nothing"))
room1 = Room(1, "room1", "text", ("action"))
room2 = Room(2, "room2", "text", ("action"))
room3 = Room(3, "room3", "Corridor to the airlock.", ("Take spacesuits", "Do nothing"))
room4 = Room(4, "room4", "text", ("action"))
room5 = Room(5, "room5", "text", ("action"))
room6 = Room(6, "room6", "text", ("action"))
room7 = Room(7, "room7", "text", ("action"))
room8 = Room(8, "room8", "text", ("action"))
room9 = Room(9, "room9", "text", ("action"))
room10 = Room(10, "room10", "text", ("action"))
room11 = Room(11, "room11", "text", ("action"))
room12 = Room(12, "room12", "text", ("action"))
room13 = Room(13, "room13", "text", ("action"))
room14 = Room(14, "room14", "text", ("action"))
room15 = Room(15, "room15", "text", ("action"))
room16 = Room(16, "room16", "text", ("action"))
room17 = Room(17, "room17", "text", ("action"))
room0.set_directions(None, room3, None, None)
room1.set_directions(None, room4, room2, None)
room3.set_directions(room0, room6, None, None)


def performaction(currentroom, action, inventory):
    print(inventory)
    if currentroom == room0:

        if action == "1":
            print("You stare into the abyss..")

        elif action == "2":
            if "spacesuit" in inventory:
                print("You put on the spacesuit and head outside. There is an apparent coldness but you are protected by the suit.\nAsteroids drift by, sometimes knocking into your ship and producing scary sounds. You see systems broken from the accident, electricity flickering in the darkness.")
            else:
                print("You have no spacesuit.")


    elif currentroom == room3:
        if action == "1":
            inventory.append("spacesuit")

    return inventory


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def intro():
    print("After 11 years serving aboard the -ship name-, the Second War of Jupiter has finally come to a close.")
    time.sleep(3)
    print("It's time to head home.")
    time.sleep(1)
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
    input("Press enter to begin..")


def playgame():
    currentroom = room0
    inventory = []
    gameover = False
    health = 30
    # intro()

    while not gameover:
        print("\n" + currentroom.description)

        for i, action in enumerate(currentroom.actions):
            print("{0}: {1}".format(i+1, action))

        chosenaction = input("What do you do? ")
        print(inventory)
        inventory = performaction(currentroom, chosenaction, inventory)
        direction = input("Where do you go? ")
        currentroom = currentroom.move(interpretinput(direction))


playgame()
