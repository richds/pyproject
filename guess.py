import random 
secretNumber = random.randint(1,10)

print("I am thinking of a number between 1 and 10")
guesscount=1
maxGuesses = 5

while(guesscount <= maxGuesses):
    print("Take a guess")
    guess = int(input())
    if guess == secretNumber:
        print("That's right! You guessed it in " + str(guesscount)+ " guesses")
        break
    elif guess < secretNumber:
        print("Sorry, that's not correct, try a higher number")
    else:
        print("Sorry, that's not correct, try a lower number")
    if guesscount == maxGuesses:
        print("You have failed this task, Paduan")

    guesscount += 1
    
