current_movies = {'The Grinch':'11:00',
'Rudolph':'1:00', 'Frostly the Snowman':'3:00', 'Christmas Vacation':'5:00'}

print("We're showing the following movies:")
for key in current_movies:
    print(key)

movie = input('What movie wold you like the showtime for?\n')

showtime = current_movies.get(movie)

if showtime == None:
    print("Requeste movie isn't playing")
else:
    print(movie + ' is playing at '  + showtime)