import os

def find_acronym():
    look_up = input("What software acronym would you like to look up?\n")
    # open the file
    file_path = os.path.join(os.path.dirname(__file__), 'file.txt')
    found = False
    try:
        with open(file_path) as file:
            # read the file
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print('File not found')
        return 
        
    if not found:
        print('The acronym does not exist')
        
def add_acronym():
    #ask the user what acronym they want to add
    acronym = input('What acronym do you watn to add?\n')
    #ask the user for the definition 
    definition=input('What is the definition?\n')
    #open the file
    file_path = os.path.join(os.path.dirname(__file__), 'acronym.txt')  #clarify the path 
    with open(file_path, 'a') as file:
    #write the new acronym and definition to the file
        file.write(acronym + '-' + definition + '\n')

def main():
    #ask the user whether they want to find or add an acronym 
    choice = input('Do you want to find (F) or add(A) an acronym?')
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()

main()

