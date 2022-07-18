#################################################
# Code Tutorial
#
#
#
#
# Items: sword(good), pet-tiger(good), poison(bad), books(good), (knife), bottle of blood(good),
#WE NEED CLASS WITH 2 THINGS INSIDE
#.
#
#TODO:
#Add commands (rooms, exit, leave(like leave room), inventory, etc; ) (Display rooms when choose room)
#Add classes (room or player)
#Remove lists with (remove) so there are no dupes in a room!
#
#Probably make an action while thing so you can type move, exit, rooms, stuff like that(Like if someone types move, then it can show the "Choose a room" command. Thoughts?)
#If in inventory then dont display that item from list
#
# https://sites.google.com/csedge.org/team-edge-web-python/term-0/lab-78-dictionaries/project-choose-your-own-adventure?authuser=0
###################################################
from random import randint
randint(0,10)
import os


#os.system("clear")
class x:
    def __init__(self, anything):
        self.anything = "text"


class Room:
    def __init__(self, name, items):
        self.name = name
        self.items = items


class Rooms:
    def __init__(self, rooms):
        self.rooms = rooms


## TO DO
#
welcome_prompt = ("wElcoMe t0 mY coll3ct G@me")
print(welcome_prompt)

username = input("\nEnter username:")
print("Welcome " + username)

print(
    "There are 4 rooms you are able to navigate in, start in whichever room you want dude\n"
)

print("You are now going to choose a room: \n")


# magicWandLocation = randint(1,4)
# if magicWandLocation == 1:
#   Courtyard.items.append("magic wand")

list1 = ["cat", "flame-thrower"]
list2 = ["tiger", "potion",]
list3 = ["books", "shoes", "disco-ball"]
list4 = ["sword", "barbell"]
magicWandLocation = randint(1,4)
if magicWandLocation == 1:
  list1.append("magic wand")
elif magicWandLocation == 2:
  list2.append("magic wand")
elif magicWandLocation == 3:
  list3.append("magic wand")
elif magicWandLocation == 4:
  list4.append("magic wand")
  
Gym = Room("Gym",list4)
Courtyard = Room("Courtyard", list1)
Laboratory = Room("Laboratory", list2)
Bigoyard = Room("Bigoyard", list3)
Rooms = Rooms([Gym, Courtyard, Laboratory, Bigoyard])



# Courtyard = ["cat", "flame-thrower"]
#Gym = ["barbell", "sword"]
#Laboratory = ["tiger", "potion", "magic wand"]
# Bigoyard = ["books", "shoes", "disco-ball"]

inventory = []
playing = True


def enterArea(area):
    global playing
    os.system("clear")
    print("Welcome to the " + area.name + " !!!")
    print(area.name + "Items:\n")
    for item in area.items:
        print(item)
    item = input("\nChoose an item:\n")
    if item in area.items:
        inventory.append(item)
        print(item + " chosen!\n")
        print("Inventory:\n" + str(inventory))
    if "magic wand" == item:
        playing = False
        print("You found the magic wand! You win! HOLY **** WWWWWW")
    elif item not in area.items:
        print("\nThis item isn't in this room!\n")


while playing:

    # print("Rooms")
    # for room in rooms:
    #   print(room)
    if playing == False: 
        break

    for room in Rooms.rooms:
      print(room.name)
    pickedRoom = input("\nChoose a room:")


    if (pickedRoom not in Rooms.rooms):
        print("Room not valid dude :( ")
    print("\n")  
    for room in Rooms.rooms:
      if pickedRoom == room.name:
        enterArea(room) 
        
    # if (pickedRoom in "Gym"):
    #     enterArea(Gym)

    # if (pickedRoom == "Courtyard"):
    #     enterArea(Courtyard)

    # if (pickedRoom == "Laboratory"):
    #     enterArea(Laboratory)

    # if (pickedRoom == "Bigoyard"):
    #     enterArea(Bigoyard)
print("You won kid")
