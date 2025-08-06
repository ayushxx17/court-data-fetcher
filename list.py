"""# List --> that store set of values. just like arrays
# we can store element of diff types.

marks = [92.1, 84.9, 78.9, 78.4, 69.6]
print(marks)
print(type(marks))
print(len(marks))

print(marks[0])
print(marks[2])

student = ["ayush", 96.1, 17, "Gaya"]
print(student[0])
student[0] = "ayushh"
print(student)

# list slicing. list_name(starting_idx : end idx)
marks = [77,81,87,84,92]
print(marks[1:5])"""

# list methods
list = [2,1,1,4]

list.append(8)             #add one element at end.
print(list)
list.sort()                #sort in assending oreder.
print(list)
list.sort(reverse=True)    #sort in desending order.
print(list)
list.reverse()             #reverse list
print(list)
list.insert(2,4)           #insert element at index
print(list)
list.remove(1)             #remove 1st occuerence of element.
print(list)
list.pop(3)                #remove element at index.
print(list)