#guess the number game
import random

guessesTaken = 0

#ask user name
print("Hello, what is your name?")
#store user name
user = input()

#generate random number between 1-20
number = random.randint(1,20)
#greet user
print("Hello, " + user + ", I am thinking of a number between 1 and 20.")

#loop for 6 tries
for guessesTaken in range(6):
    print("Take a guess.")
    guess = input()
    #parse input string as int to compare with random number
    guess = int(guess)

    if guess < number:
        print("Your guess is too low.")
    if guess > number:
        print("Your guess is too high")
    if guess == number:
        break
#check if user's answer is true after loop is done
if guess == number:
    #convert guessesTaken + 1 to string so strings can be concatenated. Python stings can only be concatenated with other strings
    guessesTaken = str(guessesTaken + 1)
    print(user + ", you guessed my number in" + guessesTaken + " guesses." )
#check if user's answer is false
if guess != number:
    #convert number to string so it can be concatenated with other strings
    number = str(number)
    print("you got it wrong! The number I was thinking is: " + number + ".")