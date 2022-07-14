#############################################################################
 #                                                                  
 #  Team Edge dictionaries: Dictionaries CHALLENGES 
 # 
 #  For this activity, you will be building a dictionary and with properties
 #  and methods. You will access the properties, set new values, and use
 #  the methods to change your dictionary state. What dictionary? Ask your coach.
 # 
 #  1. DEFINE: Make a dictionary and set its properties, printing changes in between.
 #  2. MODIFY: Add 2 new properties and assing values. Change existing values,
 #     including adding or updating values inside lists
 #  3. METHODS: Now its time to make some methods tha can make a change
 #     to your values, like a boolean, or they can print something about
 #     the dictionary. Nothing fancy, unless you fancy it.
 #  4. LITERALLY: Use string literals to put it all together in one statement.
 # 
 # #########################################################################/

print("------------------- CHALLENGE 1 : DEFINE    -------------------")

#Below is a simple example of a dictionary implementaion. 
#-->TODO: Add at least 3 comments to the dictionary below to demonstrate you understand its usage

dictionary = {
    "name": "box",
    "is_empty": True
}
#working with the dictionary:
dictionary["length"] = 12
dictionary["width"] = 8
dictionary["contents"] = ["thing 1", "thing 2", "thing 3"]
print(f"{dictionary['name']} is {dictionary['length']} {dictionary['width']}")
dictionary["contents"].append("thing 4")
print(f"{dictionary['name']} has {dictionary['contents']}")
print(dictionary)

 

#-->TODO: Declare a new dictionary and set at least 4 properties to it including: string, boolean, number, list

##################################  MY dictionary ########################### #/


new_dictionary = {
    "cows": 11,
    "nothing_here": True,
    "height" : 9,
    "nombre" : "elian"
                   

}



########################################################################## #/



print("------------------- CHALLENGE 2 : MODIFY   -------------------")

#-->TODO: Print your dictionary you created above
print(new_dictionary)

#-->TODO: Update the dictionary you just created  by adding new properties and values, including list elements, in this section.

new_dictionary["height"] = 123
new_dictionary["nothing_here"] = False
new_dictionary["nombre"] = "Zandy"
#-->TODO: Print your dictionary again and observe changes


print("------------------- CHALLENGE 3 : MEHTODS   -------------------")


#-->TODO: Make a method that will update your dictionary value. It should take in a dictionary and return it modified.
new_dictionary ={"cows": 11, "height": 5, "nombre": "sandra"}
up_dict = {"cows": 111, "height": 6, "nombre": "ELI"}
print("dictionary before updation:,new_dictionary")
new_dictionary.update(new_dictionary)
print("dictionary after updation:,new_dictionary")
#-->TODO: Call the method.

up_dict()

print("------------------- CHALLENGE 4 : LITERALLY   -------------------")

#-->TODO: Put it all together using a string literal to tell the story of your dictionary!
