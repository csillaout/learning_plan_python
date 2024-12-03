import random
#two players roll the dice and see who wins

#1
#define the function for rolling the dice
def roll_dice():
    dice_total = random.randint(1, 6) + random.randint(1,6)
    return dice_total

#2 
#ask for names
def main():
    player1 = input("What is your name?\n")
    player2 = input('What is your name?\n')

    #assign the variable
    roll1 = roll_dice()
    roll2 = roll_dice() #you have to assign it to a variable for each player

    #print the result in the console
    print(player1, 'rolled', roll1)
    print(player2, 'rolled', roll2)

    #compare the dice and print the result
    if roll1 > roll2:
        print(player1, 'won')
    elif roll2> roll1:
        print(player2, 'won')
    else:
        print('Its a TIE')

#3 you have to call the function
main()