# Modify dictionary. Each key should be the original number, and the value should be the doubled number.

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
double_list = {}

for i in list:
    double_list[i] = i*2

print(double_list)

#create a dict from a list and place each name reverse lower case
name_list = ["Csilla", "Andrea", "Dora"]
reverse_list = {}

for name in name_list:
    reverse_list[name] = name[::-1].lower()

print(reverse_list)

#search for a specific number in the list and print true if it is in 
# List of numbers
numbers = [10, 20, 30, 40, 50]

# Number to look for
target = 30

# Iterate through the list
found = False
for num in numbers:
    if num == target:
        found = True
        break

print(found)  # Output: True
