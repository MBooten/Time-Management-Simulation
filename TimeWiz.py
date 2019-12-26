#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
TimeWiz the game

TimeWiz the game is based on a riddle. This riddle requires the player to get 4 people across a bridge within
a timeframe of 15 minutes. The full riddle is printed by the function: gameStory. The game consists of 6 
interactions that check the position of in game characters and take player feedback. 
The game gives the player choices for input for character crossing and utilizes dictionaries to attach severity
to the player choices. The choices of the ingame personas function as the keys to the values in the dictionary.
When a player inputs a value, the method .upper() is used consistently to ensure capitalization. Alternatively,
the function capitalize() could have been used for this. Variables p_across are originally empty and are filled
with string values to indicate which in game character has crossed the bridge. Input is checked for duplicate
entry and entries irrelevant to the game and  the story.


Source:
https://en.wikipedia.org/wiki/Bridge_and_torch_problem

Created by Matthias Booten

"""

#####################################################################
#The function gameStart initializes the game and it's variables.
#Furthermore, the player is greeted and an inquiry on the player's name is made.
#####################################################################


#Known issues:   * A redundancy in checking for time > 15 
# The game works with this code but I believe there should be more
#effective, less code intensive solutions.
#The game catches wrongfull input, but under certain circumstances it keeps looping (without a loop)
#If I would have done it again I would have used more functions to replace the large sequences of
#if statements.

#Correct sequence is AB A CD B AB

# extra functionality: http://www.jave.de/figlet/fonts/overview.html

#This game requires you to:
#pip install pyfiglet to utilize the "Game Over" sequence ( !!! )

#This code can help you install pyfiglet if need be
#source: https://stackoverflow.com/questions/44210656/how-to-check-if-a-module-is-installed-in-python-and-if-not-install-it-within-t
#import pip

#pkgs = ['mutagen', 'gTTS']
#for package in pkgs:
#    try:
#        import package
#    except ImportError, e:
#        pip.main(['install', package])
        
import pandas
from pyfiglet import Figlet

def gameStart():
    print("Welcome to TimeWiz the game!")
    
    #Global variables of player names are declared.
    
    global A
    global B
    global C
    global D
    
    #-The player name variables are given fixed values.
    A= 1 ; B= 2; C=5; D=8
    
    #Global variable time is declared and given a value.
    global time
    time=0
    
    #Variable that checks if the game is solved is declared
    global gameSolved
    gameSolved = False
    
    #Global variables that confirm if personas in the riddle have crossed the 
    #bridge have crossed are declared. These variables are assigned a default
    #value.
    
    global p1_Across
    p1_Across=""
    global p2_Across
    p2_Across=""
    global p3_Across
    p3_Across=""
    global p4_Across
    p4_Across=""
    
    #Declares the variable of the players name and gives the player
    #the opportunity to input their player name.
    global name
    name = input(prompt = 'Input your name: ')
    
    print('Welcome ' + name + '!') #Also seems to work without f (f was from coursebook)
    input('<Press ENTER to continue>\n')

        
######################################################################
# Defines and calls the function gameStory
######################################################################

def gameStory():
    print('This game is designed to test your time management and people management skills, '+ name +'.')
    print("")
    print("""Four people arrive at a river with a narrow bridge that can only
hold two people at a time. It's nighttime and they have one torch 
that has to be used when crossing the bridge. Person A can cross the 
bridge in one minute, B in two minutes, C in five minutes, and D in 
eight minutes. When two people cross the bridge together, they must
move at the slower person's pace. \n \nCan they all get across the bridge in 15 minutes or less?""")

    input('<Press Enter key to continue>\n')
 
######################################################################
# Defines and calls the function Interaction_1
######################################################################
def Interaction_1():
    global time
    
    global p1_Across
    global p2_Across
    
    #Making Choice 1 & 2 in the first user interaction.
    print('Your first choice has come up, ' + name +'!')
    print('Please convey which set of two people will be crossing the bridge first!')
    print('Which person has to cross first?')
    
    #Player input prompts are created
    choice1= input(prompt = 'Input person A,B,C or D: ').upper()
    
    #Failsafe that guards against player inputting irrelevant content.
    if choice1 != "A" and choice1 != "B"and choice1 != "C" and choice1 != "D" :
        print("User input is limited to either \"A,B,C or D\", please try again.")
        Interaction_1()
        
    print('Which person has to join in crossing the river?')
    choice2= input(prompt = 'Pick a new person from the group of people: ').upper()
    
    #Failsafe that guards against player inputting irrelevant content.
    if choice2 != "A" and choice2 != "B"and choice2 != "C" and choice2 != "D" :
        print("User input is limited to either \"A,B,C or D\", please try again.")
        Interaction_1()
    
    #Checker to confirm the player doesn't mistakenly let's a player cross twice.     
    if choice1 == choice2:
        print("""You have to pick two different people! Please choose again.""")
        Interaction_1() 
    
    #Feedback with alternative dynamic print method.
    print("Ok, " + name + " your choices are: " + choice1 + " and " + choice2 + "!")
    
    #Converting choices into time for choice1.
    if choice1 == "A":
        p1_Across="A"
    elif choice1 == "B":
        p1_Across="B"
    elif choice1 == "C":
        p1_Across="C"
    elif choice1 == "D":
        p1_Across="D"
    else:
        print("You managed to make no valid choice, congratulations!")
        print("Try again.")
        Interaction_1()

    #Converting choices into time for choice2.
    if choice2 == "A" and choice1 != choice2:
        p2_Across="A"
    elif choice2 == "B" and choice1 != choice2:
        p2_Across="B"
    elif choice2 == "C" and choice1 != choice2:
        p2_Across="C"
    elif choice2 == "D" and choice1 != choice2:
        p2_Across="D"
    else:
        print("Please don't select the same person twice and try again!")
             
   #In the case of a person being selected twice, the interaction has to be reset.     
        Interaction_1()
        
   #If a correct choice has been made, the time of crossing has to be calculated.
   #This is done based on choice gravity dictionary ch_Grav and the implication of said choice.
    if choice1 != choice2:  
        ch_Grav={"A" : 1, "B" : 2, "C" : 5, "D" : 8}
   
        value1=ch_Grav[choice1]
        value2=ch_Grav[choice2]
    
        if value1 > value2:
            implication=value1
        else:
            implication=value2
    
        time=time+implication
    
        print("Your time is " + str(time) + " minutes.")
    
    else:
        print("")

######################################################################
# Defines and calls the function Interaction_2
######################################################################
def Interaction_2():
    global time
    global p1_Across
    global p2_Across
    
    print("")
    print("Your first two people have crossed the bridge, congratulations!")
    print(f"""Now that {p1_Across} and {p2_Across} are on the other side, someone has to bring
back the light to cross the bridge! Who will you choose?""")

    #Player is offered a tactical choice of whom will go back
    choice3=input(prompt = f'Pick either person {p1_Across} or person {p2_Across} to go back. ').upper()
    
    #Failsafe that guards against player inputting irrelevant content.
    if choice3 != "A" and choice3 != "B"and choice3 != "C" and choice3 != "D" :
        print("User input is limited to either \"A,B,C or D\", please try again.")
        Interaction_2()
        
    #Checks player choice for logic.
    if choice3 != p1_Across and choice3 != p2_Across:
        print("Sorry, you can only pick a person from those that have crossed the bridge.")
        Interaction_2()  
    else:
        print("Alright!")      
        print(f"You chose person {choice3}, great!")
    
    #Calculating the implication of choice 3 on the time
    #This is done only when the if-statement is fullfilled to avoid unrightfull deleting of p2_Across.
    
    if choice3 == p1_Across or choice3 == p2_Across:
        ch_Grav={"A" : 1, "B" : 2, "C" : 5, "D" : 8}
        value=ch_Grav[choice3]
        time=time+value
    
        print("Your time is " + str(time) + " minutes.")
    
        if choice3 == p1_Across:
            pers_Remaining = p2_Across
        elif choice3 == p2_Across:
            pers_Remaining=p1_Across
        
        p1_Across=pers_Remaining
        p2_Across=""
    
        print("The only person left on the other side of the bridge is person "+ p1_Across + ".")
    else:
        print("something went wrong, restart please.")
        Interaction2_()        
    if time > 15:
        Interaction_6()
        
######################################################################
# Defines and calls the function Interaction_3
######################################################################
def Interaction_3():
    global time
    global p2_Across
    global p3_Across
    
    print("")
    #Player is offered extra information and a set of choices for the game characters. 
    print(f"""Alright {name}, {p1_Across} is still on the other side and it is time
to chose which of his buddies has to cross next. Remember that time is of
the essence as you strive to keep your time under 15 minutes. Also, do keep
in mind that no more than 2 people  can cross the bridge at a time.\n
Whom do you choose to cross the bridge next?""")
    
    #Player is offered a tactical choice.
    choice4 = input(prompt = 'Input your first choice regarding whom has to cross first: ').upper()
        
    #Failsafe that guards against player inputting irrelevant content.
    if choice4 != "A" and choice4!= "B"and choice4 != "C" and choice4 != "D" :
        print("User input is limited to either \"A,B,C or D\", please try again.")
        Interaction_3()
    
    #Player is offered a tactical choice.
    choice5 = input(prompt = 'Input your choice regarding whom has to cross next: ').upper()
    
    #Failsafe that guards against player inputting irrelevant content.
    if choice5 != "A" and choice5 != "B"and choice5 != "C" and choice5 != "D" :
        print("User input is limited to either \"A,B,C or D\", please try again.")
        Interaction_3()
        
    #Failsafe that checks if a player accidentally picks a person on the wrong side of the bridge
    if choice4 == p1_Across or choice5 == p1_Across:
        print(f"""{p1_Across} is already on the other side of the bridge! Please choose again.""")
        Interaction_3()
    
    #Failsafe that checks for double input.
    elif choice4 == choice5:
        print("""You have to pick two different people! Please choose again.""")
        Interaction_3()

    #Calculating the implication of choice 4 on the time utilizing the right gravity/severity of time. 
    if   choice4 != p1_Across and  choice5 != p1_Across and choice4 != choice5: 
        ch_Grav={"A" : 1, "B" : 2, "C" : 5, "D" : 8}
    
        value1=ch_Grav[choice4]
        value2=ch_Grav[choice5]
    
        if value1 > value2:
            implication=value1
        else:
            implication=value2
    
        time=time+implication
    
        p2_Across=choice4
        p3_Across=choice5
    
        print(f'The time that has passed is: {time} minutes.')
    else:
        print("something went wrong, restart please.")
        Interaction3_()
    if time > 15:
        Interaction_6()

######################################################################
# Defines and calls the function Interaction_4
######################################################################
def Interaction_4():
    global time
    global p1_Across
    global p2_Across
    global p3_Across
    
    print("")
    #The player is updated on which character is across the bridge and presented his options.
    print(f"""Person {p1_Across},{p2_Across} and {p3_Across} have now crossed the bridge.
Now it is time to have the last person cross the bridge. Remember that in order to cross the bridge,
a light  is needed. Whom do you choose to bring back the light for the final crossing? Your choice
includes all the people that have crossed the bridge already. """)

    #The layer is asked input his choice
    choice6 = input(prompt = 'Which person do you choose to bring back the light for the final crossing?> ').upper()
    
    #Failsafe that guards against player inputting irrelevant content.
    if choice6 != "A" and choice6 != "B"and choice6 != "C" and choice6 != "D" :
        print("User input is limited to either \"A,B,C or D\", please try again.")
        Interaction_4()
        
    #Failsafe check to avoid the player choosing someone whom is already across the bridge.
    if choice6 != p1_Across and choice6 != p2_Across and choice6 != p3_Across:
        print(f"""Person {choice6} has not crossed the bridge yet. This person can not bring
back the light.\n Please make a new choice.""")
        Interaction_4()
   
    #The dictionary containing the key and value set to the severity of the player's decisions
    #is consulted. The gravity/severity of the player's decission is applied to the time.
    if choice6 == p1_Across or choice6 == p2_Across or choice6 == p3_Across:
        ch_Grav={"A" : 1, "B" : 2, "C" : 5, "D" : 8}
        value=ch_Grav[choice6]
    
        time=time + value
    
        print(f"""The total passed time is: {time} minutes.""")
    
    #A list is created so that chronological order can be maintained of people
    #that have crossed.
        tempListCrossed = []
   
        #print(choice6, p1_Across, p2_Across,p3_Across) optional check: choice vs across
        if choice6 != p1_Across:
            tempListCrossed.append(p1_Across)
        if choice6 != p2_Across:
            tempListCrossed.append(p2_Across)
        if choice6 != p3_Across:
            tempListCrossed.append(p3_Across)
        else:
            print("Strangly, choice 6 is not in there.")
            Interaction_4()
        p1_Across=tempListCrossed[0]
        p2_Across=tempListCrossed[1]
        p3_Across=""
    
    print(f"""The people that have crossed include: {p1_Across} and {p2_Across}.""")
    
    if time > 15:
        Interaction_6()
    
######################################################################
# Defines and calls the function Interaction_5
######################################################################
  
  ###
  # This function allows the player to move the final pair of people across the bridge.
  ###
def Interaction_5():
    global time
    
    print("")
    #The player is presented information in order to make a choice on which pair shall cross.
    print(f"""Your final decision has come up, {name}. \n
Person {p1_Across} and {p2_Across} have already made it across the bridge \n
Now it is time for your last pair to cross over! Can you remind me of their names?""")
    
    #The player is offered a tactical choice.
    choice7 = input(prompt = 'Name of person 1: ').upper()
    
    #Failsafe that guards against player inputting irrelevant content.
    if choice7 != "A" and choice7 != "B"and choice7 != "C" and choice7 != "D" :
        print("User input is limited to either \"A,B,C or D\", please try again.")
        Interaction_5()
    
    #The player is offered a tactical choice.    
    choice8 = input(prompt = 'Name of person 2: ').upper()
    
    #Failsafe that guards against player inputting irrelevant content.
    if choice8 != "A" and choice8 != "B"and choice8 != "C" and choice8 != "D" :
        print("User input is limited to either \"A,B,C or D\", please try again.")
        Interaction_5()
    
    #A failsafe to avoid accidental double entry.
    if choice7 == choice8:
        print("""You have to pick two different people! Please choose again.""")
        Interaction_5()
    
    #Ensures the player doesn't chose a character on the wrong side of the bridge.    
    elif choice7 == p1_Across or choice7 == p2_Across or choice8 == p1_Across or choice8 == p2_Across:
        print("redo")
        Interaction_5()
   
     #Adds meaning to the players choice by using the player's choice as a key to access the time value.
     #The time value is then updated based on the player's choice.
    if choice7 != p1_Across and choice7 != p2_Across and choice8 != p1_Across and choice8 != p2_Across:
        ch_Grav={"A" : 1, "B" : 2, "C" : 5, "D" : 8}
    
        value1=ch_Grav[choice7]
        value2=ch_Grav[choice8]
    
        if value1 > value2:
            implication=value1
        else:
            implication=value2
    
        time=time+implication
        p3_Across = choice7
        p4_Across = choice8
    else:
        print("something went wrong, restart please.")
        Interaction_5()
        
        print("It took you " + str(time) + " minutes.")
    
    
######################################################################
# Defines and calls the function Interaction_6
######################################################################
  
  ###
  # This function allows the player to move the final pair of people across the bridge.
  ###
def Interaction_6():
    global time
    global gameSolved
    
    print("")
    #Checks if time is less than 15 minutes and confirms if the player has won or lost the game.
    if time <= 15 :
        print("Congratulations! You solved the game!!")
        gameSolved=True
    elif time > 15:
        print("Dundunduuuun")
        print('Game over! You went over time!')
        fText="Game Over"
        f=Figlet(font='slant')
        print(f.renderText(fText))


    
gameStart() # This function starts the game
gameStory() # This function conveys the story of the game


Interaction_1() #This function enables the player to make the first interaction
while time < 15:
    Interaction_2()#Enables the, player to make a choice on who to send back with the torch.
    while time < 15:
        Interaction_3()#Enables the player to choose the next pair of people to cross the bridge.
        while time < 15:
            Interaction_4()#This function enables the player to make a choice on who to send back with the torch
            while time < 15:
                Interaction_5()#This function allows the player to move the final pair of people across the bridge.
                while time <= 15 and gameSolved == False:
                    Interaction_6()#The final function interacts with the player to inform them on their final game status.
    

