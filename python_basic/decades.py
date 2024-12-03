age=int(input("How old are you?\n"))

decades = age//10   #this gives you the int 
years = age % 10   #this gives you the remaining amount

print("you are " + str(decades) + " decades and " + str(years)+ " years old.")