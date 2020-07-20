import random
import time

#Set up random number with while loops, which if number is too high and too low and how many guesses they have remaining
def guessGame(limit, number):
    random_number =  random.randint(1, number)
    try:
        while limit > 0:
            guess = int(input('What is your guess: \n'))
            limit -= 1
            if random_number == guess:
                print('You got it right!')
                break
            elif guess > random_number:
                print('That is too high, try again')
                time.sleep(1)
                print(f'You have {limit} guess(es) left')
            elif guess < random_number:
                print('That is too low, try again')
                time.sleep(1)
                print(f'You have {limit} guess(es) left')
        print('Game over')
        print(f'The random number was {random_number}')
    except ValueError:
        print('Only integers are allowed')
    
#Set up the rules for each difficulty        
def easy():
    print("You are to guess a number between 1 and 10, and you have 6 guesses")
    guessGame(5, 10)
    
def medium():
    print("You are to guess a number between 1 and 20, and you have 5 guesses")
    guessGame(5, 20)
    
def hard():
    print("You are to guess a number between 1 and 50, and you have 4 guesses")
    guessGame(4, 50)

#Set up function on if they want to play again after they game is over with upper or lower case answer    
def playAgain():
    again = input('Do you want to play again? Yes/No \n')
    if again.upper() == 'YES':
        start()
    elif again.upper() == 'NO':
        print('Thanks for playing!')
        exit()
    else:
        print('Wrong input')
        playAgain()

#open program with asking for their name
name = input("What is your name: \n")
time.sleep(2)
print("Welcome", name + "!")
time.sleep(2)

#After they get their name, we start the game asking to choose the level with upper or lower case answer
def start():
    print('Welcome to the guessing game!!!')
    difficulty = input( "Choose your difficuly between Easy, Medium and Hard: \n")
    if difficulty.upper() == "EASY":
        easy()
        playAgain()
    elif difficulty.upper() == "MEDIUM":
        medium()
        playAgain()
    elif difficulty.upper() == "HARD":
        hard()
        playAgain()
    else:
        print('Wrong input')
        start()
        

start()