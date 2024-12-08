#Leroy
#Simulate 20 sided dice roll for DnD, This is a short dice roll game simulating a
#basic monster fight
#Player must choose to attack or flee and then must roll a high enough random
#number to win
#10/9/2024
import random

D20 = random.randrange(1, 20)#This is a simulated 20 sided dice roll
print("You are walking down a path when a Demigorgan suddenly leaps from the bushes!: ")
inp = input("You must attack or flee: ")
while inp != "flee" and inp != "attack":
    print("You must choose between attack or flee")#This will repeat if neiter option is typed
    inp = input("You must attack or flee: ")
if inp == "flee":
    print("You chose to flee! You live to fight another day!")
# This is the flee option, player escapes and progam exits
elif inp == "attack":
    print("You chose to attack!") # This is the attack option, player must now
    #roll to beat the armor of Demigorgan
    print("Draw your weapon and strike! Roll a D20, you must roll a 14 or better to defeat it.")
    print("You rolled a: ")
    print(D20)#Random dice roll of D20, To win the player must roll a 14 orhigher
    if D20 <= 13:
        print("The Demigorgan blocks your attack and bites off your head!")
    elif D20 >= 14:
        print("You slayed the Demigorgan! You are a hero!")
    
inp = input("Type Enter to Exit")
#####################

