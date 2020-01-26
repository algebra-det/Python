# Hangman game

import random , time

name = input("Enter your name - ")
print("Hello !",name[0].upper()+name[1:],", Let's get this game started ")
time.sleep(1)
print("Here we have a word for you related to bollywood movie\nguess by character")
time.sleep(5)
lst = ['chamku','kabuliwala','jimmy','parineeta','contract','wednesday','rafoochakkar','drohkaal','nastik','paheli','showbiz','utthaan',
        'waris','anwar','eklavya','fareb','dashavatar']
word = random.choice(lst)
print(word)
guesses = ''
turn = 10
copy = []
while turn>0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("-")
            failed+=1
    print("You have %d turns left " % (turn))
    if failed==0:
        print("")
        print("Congratulation ! You won the game")
        print("Aap Jeet chuke hai 1 crore rupey")
        break
    print()
    guess = input("Enter a character")
    guesses += guess[0]
    copy.append(guess[0])
    if guess[0] not in word:
        print("Wrong")
        turn-=1
        if turn==0:
            print("Game Over")
            print("You didn't get the word")
            print("The word is - ",word)
    print("You have used ",copy)
