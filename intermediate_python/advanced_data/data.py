#set creation
my_set = {1,2,3,4}
empty_set = set()

set1 ={1,2,3}
set2={3,4,5}
print(set1 | set2) #{1,2,3,4,5}
print(set1 & set1) #{3}
print(set1 - set2) #{1,2}

set1.add(13)
print(set1)
set2.remove(5)
print(set2)

#frozen set
my_frozenset = frozenset([1,2,3,4])

#nested data structure
nested_list = [[1,2], [3,4], [5,6]]
print(nested_list[1][0]) #access 3

#iterating ghrough nested data
for sublist in nested_list:
    for item in sublist:
        print(item)

#list of dict
employees = [{"name": "Alice", "age": 40}, {"name":"Bob", "age": 50}]
print(employees[1]["name"]) #access Bob

#dict of dict
nested_dict = {"person1": {"name": "Alice", "age": 30}, "person2": {"name": "Bob", "age": 25}}
print(nested_dict["person1"]["age"])  # Accesses 30

#exercise 1
set3={1,2,3,4,5,6}
set4 = {6,7,8,9,0}

intersection = set3&set4
print(intersection) #{6}
union = set3 | set4
print(union) #{0,1,2,3,4,5,6,7,8,9}
difference = set3^set4 
print(difference) #{0,1,2,3,4,5,7,8,9}

#exercise2 parsing nested lists
#given a nested list of integers, write a function to flatten it itno a single list of integers
def flatten():
    main_list=[[1,2],[3,4],[5,6]]
    flat_list =[]
    for sublist in main_list:
        for item in sublist:
            flat_list.append(item)
    print(flat_list)

flatten()

# Analyzing a Nested Dataset: Given a list of dictionaries containing product data, calculate the total inventory value (price multiplied by quantity for each product).

products = [
    {"name": "Laptop", "price": 1000, "quantity": 5},
    {"name": "Phone", "price": 500, "quantity": 10},
    {"name": "Tablet", "price": 300, "quantity": 7}
]

def total_inventory_value(products):
    total_value = 0
    for product in products:
        total_value += product["price"] * product["quantity"]
    return total_value

print(total_inventory_value(products))  # Output: Total inventory value
