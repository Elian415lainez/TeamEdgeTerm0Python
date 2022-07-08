import random

# -------------------------------------------- 

	# You've just learned about variables, conditionals.
	# Just from knowing those two topics, you can do so much!
	
	# Let's try to make a simple program that responds to the user.
	# We're going to recreate the Magic 8 Ball!!!
			
			# Never heard of it? That's ok!

					# You got this!

  # -------------------------------------------- 

	# How a Magic 8 Ball Works:

	# The user asks a question and vigoriously shakes the ball. 
	# Then the ball will respond with one of twenty responses, chosen at random. 

	# That's pretty simple right?

 # -------------------------------------------- 

	# Part 1: 
	# Print instructions on the screen and 
	# prompt the user to ask a question

	

  # --------------------------------------------

#prompt_user = ("Pick a color please, any color ")
#number = (0,9)
#print (prompt_user)
#print (" Here are the colors you can choose from ")
#print ("green, red, blue, yellow")
#color = input("choose color")
#print (color)

#if color == "red":
	#number == input(" enter number 1 or 2")
#elif color == "green":
	#number == input(" enter number 3 or 4")
#elif color == "blue":
	#number == input(" enter number 5 or 6")
#elif color == "yellow":
	#number == input("enter number 7 or 8")


color= ['red', 'green', 'blue', 'yellow']
prompt_user = ("Pick a given color and a number from 1 to 8")
number = (0, 9)
print (prompt_user)
choosen_color= input("Enter either red or green or blue or yellow: ")
if choosen_color == "red": 
    number = input("Enter a number from 1 or 2: ")
    if int(number) == 1:
        print ("You will be a writer!")
    elif int(number) == 2:
        print ("You will be a singer!")
if choosen_color== "blue":
    number= input("Enter a number from 3 or 4: ")
    if int(number) == 3:
        print ("You will be a doctor!")
    if int(number) == 4:
        print ("You will be a lawyer!")
if choosen_color== "green":
    number= input("Enter a number from 5 to 6: ")
    if int(number) == 5:
        print ("You will be a coder!") 
    if int(number) == 6:
        print ("You will be a constructor!")
if choosen_color== "yellow":
    number = input("Enter a number from 7 to 8: ")
    if int(number) == 7:
        print ("You will be an artist!")
    if int(number) == 8:
        print ("You will be a teacher!")
else: 
    print ("Read the direction!!!!!!")
















# -------------------------------------------- 

	# Part 2: Next, we need to randomly select a response from 20 options.

	# Randomly select a number from 0 - 19 
	# Use that to select from the following responses:
		# 0 - It is certain.
		# 1 - It is decidedly so.
		# 2 - Without a doubt.
		# 3 - Yes - definitely.
		# 4 - You may rely on it.
		# 5 - As I see it, yes.
		# 6 - Most likely.
		# 7 - Outlook good.
		# 8 - Yes.
		# 9 - Signs point to yes.
		# 10 - Reply hazy, try again.
		# 11 - Ask again later.
		# 12 - Better not tell you now.
		# 13 - Cannot predict now.
		# 14 - Concentrate and ask again.
		# 15 - Don't count on it.
		# 16 - My reply is no.
		# 17 - My sources say no.
		# 18 - Outlook not so good.
		# 19 - Very doubtful.

	# Look up random.rand_int to see how you can use it to select a random number.

  # -------------------------------------------- 




















# -------------------------------------------- 

	# Part 3: Customize it!

	# Select your own theme and use case and modify your code!
	
# -------------------------------------------- 

















