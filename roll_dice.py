import random #import random module it allows to use its function in our program

roll = random.randint(1,6) #calls a random int between 1 and 6

#guess the number the computer will roll:
guess = int(input("Guess the dice roll:\n"))

if guess == roll:
    print("Correct! They rolled a  " + str(roll))  #use conditional statement to compare the guess with the roll and concatenate the rolled number out
else:
    print("Wrong answer! They rolled a " + str(roll))