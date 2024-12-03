import random #importing random to be able to use its function

computer_choice = random.choice(['rock', 'paper','scissors'])
user_choice=input("Do you want rock, paper, or scissors?\n") #set up a user choice but asigning a variable with an input

#print out the compute_choice to see what it was
print(computer_choice)

#now figure out who the winner is?
if computer_choice==user_choice:
    print("TIE")
elif user_choice=='rock' and computer_choice=='scissors':
    print("WIN")
elif user_choice=='paper' and computer_choice=='rock':
    print("WIN")
elif user_choice=='scissors' and computer_choice=='paper':
    print("WIN")
else:
    print("YOU LOOSE COMPUTER WINS")