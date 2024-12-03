# Given a list of numbers, double all the numbers using a loop, and store the results in a new list.

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
double_list=[]
for i in list:
    double_list.append(i*2)

print("original list:", list)
print("doubled list:", double_list)