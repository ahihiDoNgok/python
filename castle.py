#step 1: user is prompted to pick a room
#step 2: need to provide a brief description in the room
#step 3: if they choose to exit, they can leave the game
#step 4: needs to be at least 6 rooms - not every room is reachable
#step 5: game needs alternate endings w/ random death generator

import random
#random death generator
death_number = random.randint(1,100)

#define loop control
room = 1

print()
print("Welcome to Hogwarts, the school of Witchcraft and Wizardry!")
print("You have been given the chance to help Harry Potter and his friends find one of Lord Voldemort's Horcruxes: Tom Riddle's Diary!")
print("However, you must be careful! Lord Voldemort has his followers, Death Eaters, and many other dangerous creatures inside the castle!")
print("Be prepared and have your wand ready! Danger may appear at anytime!")
print("If by any chance you cannot continue to help Harry Potter save Hogwarts, you can enter 'exit' at anytime during your mission.")
print("Tip from creator: To experience this game fully, you may choose to listen to 'Hedwig's Theme' while playing. Good luck!")
print()

while room != 0:
    if room == 1:
        print("You have entered the castle and are currently in the Great Hall.")
        print("The hall is grand and has rows of tables facing the stage in the front. The hall is in ruins, bodies everywhere, all leading to two doors.")
        print("The two doors journey to two different parts of the castle, one to the Gryffindor 'Common Room' and one to the 'stairs'.")
        the_choice = input("Which room would you like to venture into? ")
        if the_choice == 'Common Room':
            print("You ran into a Death Eater and have been killed on the spot. RIP")
            room = 0
        if the_choice == 'stairs':
            room = 2
            death_number = random.randint(1,100) #random chance of death
            if death_number < 15:
                print("You have been killed by a nasty Death Eater.") #outcome if death_number is < 15
                room = 0
        if the_choice == 'exit': #the exit code - the user will be taken out of the game
            room = 0

#outcome when selecting 'stairs'
    elif room == 2:
        print()
        print("You have entered the stairway. The moving paintings are all silent or empty, they have all disappeared to avoid the battle.")
        print("You see textbooks, school supplies, and wands scattered across the stairs; none of which are useful to you.")
        print("As you slowly approach the stairs, you see that you can go down to the 'dungeon' or up to the Headmaster's 'office'.")
        print()
        the_choice = input("Which room would you like to enter? ")
        if the_choice == 'dungeon':
            print("You were killed by trolls in the dungeon.")
            room = 0
        elif the_choice == 'office':
            room = 3
            death_number = random.randint(1,100)
            if death_number > 85:
                print("You have been found by Nagini, Voldemort's pet snake. She kills you instantaneously.") #outcome if death_number > 85
                room = 0
        if the_choice == 'exit':
            room = 0

#outcome for selecting 'office'
    elif room == 3:
        print ()
        print("As you enter the Headmaster's office, you walk past an empty bird cage with ashes.")
        print("The Headmaster's office is filled with books and quills. You notice how messy it is, the papers scattered everywhere.")
        print("You examine the papers trying find a map of Hogwarts, but alas, you only find student files and a blank piece of folded parchment paper.")
        print("There are painting of the past Headmasters on the walls and as you continue on, you approach a 'closet' and the Headmaster's 'bathroom'.")
        print()
        the_choice = input("Which room would you like to enter? ")
        if the_choice == 'closet':
            room = 4
            death_number = random.randint(1,100)
        elif the_choice == 'bathroom':
            if death_number > 90:
                print("You were attacked by a frightened house elf. RIP") #outcome if death_number > 90
                room = 0
            else:
                room = 5
                death_number = random.randint(1,100)
                if death_number < 35:
                    print("You have been killed by a nasty Death Eater") #outcome if death_number < 35
                    room = 0
        if the_choice == 'exit':
            room = 0

#outcome for selecting 'closet'
    elif room == 4:
        print()
        print("As you open the closet door, you see a narrow staircase the leads towards the bottom of the tower.")
        print("When you reach the end of the staircase, you are faced with two doors, one on your left and one on your right.")
        print("The door on your right has a snake symbol above it while the door on your left has a lion.")
        print()
        print("Using your previous knowledge of the origins of Tom Riddle's diary, do you choose the 'snake' door or 'lion' door.")
        the_choice = input("Which door do you choose? ")
        if the_choice == 'lion':
            print("As you enter the dark room, the door slams behind you locking you inside. There is no way out. RIP ")
            room = 0
        elif the_choice == 'snake':
            print()
            print("You enter the room and notice toarches leading you down a tunnel.")
            print("As you approach the end of the tunnel, you see on opening to your left.")
            print("You turn and see the corpse of a huge snake! This is the corpse of the basilisk that Harry Potter killed 5 years ago.")
            print("On the floor laying next to the snake is the diary of Tom Riddle!")
            print()
            print("Congrats! You have found the diary! Because of your bravery, Voldemort has been defeated and Hogwarts stands strong!")
            room = 0
        if the_choice == 'exit':
            room = 0

#outcome for selecting 'bathroom'
    elif room == 5:
        print()
        print("You enter the bathroom and notice many different cabinets")
        the_choice = input("Do you choose to open the cabinets? 'Y/N' ")
        if the_choice == 'Y':
            print("As you open the cabinet door, a poisonious spider jumps out and bites you. RIP ")
            room = 0
        elif the_choice == 'N':
            print()
            print("You turn and leave the bathroom.")
            print("However, you did not keep track of how long you were in there and did not hear the others enter the Headmaster's office.")
            print("You were greeted by werewolves who took one look at you and attacked. RIP ")
            room = 0
        if the_choice == 'exit':
            room = 0
