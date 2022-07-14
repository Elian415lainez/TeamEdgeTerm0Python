#################################################
# Code Tutorial
#
#Random items in everyroom?
#
#
# sword(good), pet-tiger(good), poison(bad), books(good), (knife), bottle of blood(good),
#
#3 items of each room
#
# https://sites.google.com/csedge.org/team-edge-web-python/term-0/lab-78-dictionaries/project-choose-your-own-adventure?authuser=0
###################################################

welcome_prompt = ("wElcoMe t0 mY coll3ct G@me")
print(welcome_prompt)

username = input("Enter username:")
print("Welcome " + username)

print("there are 4 rooms you are able to navigate in, start in whichever room you want dude")

room1 = input("welcome to the game, you are now going to choose a room")
print(room1)

rooms = ["Gym", "Courtyard", "Bigoyard", "Laboratory"]

Courtyard = ["cat","dog"]
Gym = ["barbell","sword"]
Laboratory = ["tiger", "potion", "magic wand"]
Bigoyard = ["books", "shoes", "disco-ball"]

inventory = []

def enterGym():
  print("Welcome to the gym!!!")
  print("Gym Items:")
  for item in Gym:
    print(item)
  gymItem = input("Choose a Item:")
  print(gymItem+" chosen!")
  
  
def enterCourtYard():
  print("welcome to the courtyard")
  for item in Courtyard:
    print(item)

print("Rooms:")
for room in rooms:
  print(room)


while True:
  pickedRoom = input("Choose a room:")
  if(pickedRoom not in rooms):
    print("Room not valid dude :(")
  
  if(pickedRoom == "Gym"):
    enterGym()

  if(pickedRoom == "Courtyard"):
    enterCourtYard()
    



  


  
