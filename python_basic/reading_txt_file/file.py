#Ask the user what acronym they want to look up?
look_up = input("What software acronym would you like to look up?\n").strip()
found = False

try:
    with open('file.txt', "r") as file:
        for line in file:
            # Use strip() to remove any extra newlines and make the search case-insensitive
            if look_up.lower() in line.lower().strip():
                print(line.strip())  # Print the line without the extra newline
                found = True
                break
except FileNotFoundError:
    print("The file 'file.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

if not found:
    print('The acronym does not exist')
