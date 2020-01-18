#Hangman game

import time , string
import random
name=input("Enter your name: ")
print("Hello!",name[0].upper()+name[1:], ", Time to play Hangman!") # Or str.capitalize(name[0])+name[1:]
time.sleep(1)
print("Start guessing...")
time.sleep(0.5)
lst=['expense', 'simultaneous', 'interceptor', 'gregarious', 'juxtaposed', 'ambivert', 'orifice', 'algebra','distortions','gynaecology','autonomous']
word=random.choice(lst)
guesses=''
turns=10
while(turns>0):
    failed=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed+=1
    if(failed==0):
        print(" ")
        print("Conratulations,", name, "!, You won The game")
        print("Here is your reward $ 1crore!")
        break
    guess=input("Guess a character: ")
    guesses= guesses+guess
    if guess not in word:
        turns=turns-1
        print("Wrong!")
        print("You have", turns, "turns left!")
        if turns==0:
            print("You lose!")
            print("The word was", word)

print(random.sample(lst,1))
