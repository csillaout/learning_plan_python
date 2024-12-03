import os

#where we moving our files from and to
folder_original = '/users/csillatoth/Desktop'
folder_destination = '/users/csillatoth/Desktop/CleanedUp'

#create the new CleanedUp directory
os.mkdir(folder_destination)

#in order to loop over all of the entries we need to list the entires in the desktop folder
for entry in os.scandir(folder_original):
    location_original = os.path.join(folder_original, entry.name)
    location_destination = os.path.join(folder_destination, entry.name)

    #we can move the file
    if os.path.isfile(location_original): #making sure we move files and not directories
        os.rename(location_original, location_destination)
