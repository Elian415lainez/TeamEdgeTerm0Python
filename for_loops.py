#********************************************************************
 #                                                                  
 #  Team Edge List Mini-project: FOR LOOP CHALLENGES
 # 
 #   Complete the following loop challenges below. Follow the ToDos
 #   1. COUNTER: Write a loop that prints a happy birthday message for every
 #      year you have been alive.
 #   2. ITERATOR: Write a for for loop that prints every item in a list

 #   3. EVEN COUNTDOWN: Write a for loop that counts down from 100 to 0, 
 #      printing only the odd numers
 #   4. FINDER: Write a function that takes in a list and a word and prints 
 #      CONGRATULATIONS!! if the word is found in the list
 #   5. NESTED: Write a function that logs every letter in a sentence
 # 
 # ***************************************************************/
import random

print("------------------- CHALLENGE 1 : COUNTER -------------------")

#this list prints every number between 0 and 10, using range

for x in range(11):
    print("Counter at: " + str(x))
   

#-->TODO: Write a loop that prints a happy birthday message for every year you have been alive.

for birthday in range(17):
    print("happy birthday " + str(birthday))

print("------------------- CHALLENGE 2 : ITERATOR ----------------------")

#here is a list full of colors...
colors = ['red' , 'violet' , 'cyan' , 'pink' , 'lime' , 'white' , 'yellow', 'black' , 'magenta', 'green', 'orange']

#This is how you can iterate through a list:
for x in colors:
    print("The color is: " + x)

#-->TODO: Declare a list with at least 5 animals. You provide the animals.
animals = ["dog", "cat", "dinosaur", "falcon", "badger"]

#-->TODO: Print all the animals in the array with a for loop. 

for animal in animals:
    print("the animal is a: " + animal)

print("------------------- CHALLENGE 3 : EVEN COUNTDOWN ------------------")


#The line below makes a random number between 0-50 and assigns it to the random variable
random = random.randint(0, 50)

#this if/else statement checks if the number is even using the modulo operator (%)
if random % 2 == 0:
    print(str(random) + " is even!")
else:
    print(str(random) + " is odd!")

#-->TODO: Write a function that counts BACKWARDS from 100 and prints only even numbers
#count = 100
#while count > 0:
  #print(count)
  #count = count - 1
def backward_count():
    for x in range(100,0,-2):
        print(x)

#-->TODO: Write a function that counts BACKWARDS from the given random number and prints only odd numbers
new_list = []
def backward_count1():
    for x in range(random,-1,-1):
        if(x % 2 !=  0): new_list.append(x)
    print(new_list)

backward_count1()

print("------------------- CHALLENGE 4 : Finder ------------------")

#This code uses the in operator to see if an element exists in a list. It only has to appear once.
color = input('Type a one word color and see if it is one of my favorite colors! >> ')
if color in colors:
    print("Yes, that color is a fav")
else:
    print("No, that color is not one of my favorites")

#-->TODO Declare a list of any strings you  want: cities, friends, movies, etc.
rand_strings = [1, 2, 3, 33, "The land" "michael", "jackson", "usher", "eminem", "yourself"]


#-->TODO Write function to prompt the user to "Guess" if an element is present in your list. Store their response in a variable. 
#   --> If their guess is in your list, print CONGRATULATIONS!
rand_strings = input('Guess a word ansd see if your on my guest list for todays event: ')
if x in rand_strings:
    print("yes your on my list")
else: 
    print("no your not allowed")

#-->TODO Call your function
backward_count()
print("------------------- CHALLENGE 5 : Nested ------------------")

#this is how you get the length of a word:
big_word = "antidisestablishmentarianism"
print(f"{big_word} has {len(big_word)} letters")

#this is how you can nest for loops, one inside the other! These loop through all the colors, and then through all the characters in the color
for color in colors:
#for all the colors:
    print(color)
    for c in color:
        print(" - " + c) #log each letter. Remember, a string is also an array of characters.


#-->TODO Write a function that prints every letter in a sentence that a user enters.
def print_letters(sentence):
    palabras = sentence.split(" ")
    for palas in palabras :
        for char in palas:
            print(" " + char)
sentence = input ("input a sentence and youll see every letter inside it")

#-->CHALLENGE: Let the user know which word is the shortest one!
def short_word(sentence):
    palabras = sentence.split(" ")
    return min(palabras, key=len)


print(print_letters(sentence))
print("La palabra mas corta en su parrafo es" + str(short_word(sentence)))
