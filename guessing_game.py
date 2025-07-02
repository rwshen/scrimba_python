print('Guessing game') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
def guessing_game(answer, guesses=3):
    guess = float(input("Enter your guess: "))
    if (guess == answer): 
        return "You got it!"
    else:
        if (guesses > 1):
            print("You didn't guess the number")
            return guessing_game(answer, guesses-1)
        else: 
            return "You didn't guess the number in time."


print(guessing_game(3))